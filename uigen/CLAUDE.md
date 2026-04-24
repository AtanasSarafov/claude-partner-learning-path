# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
npm run setup        # Install deps, generate Prisma client, run migrations
npm run dev          # Dev server (Turbopack) at http://localhost:3000
npm run test         # Run Vitest test suite
npm run lint         # ESLint
npm run db:reset     # Force-reset the SQLite database
npm run build        # Production build
```

To run a single test file: `npx vitest src/lib/__tests__/file-system.test.ts`

## Environment

Copy `.env` and set `ANTHROPIC_API_KEY`. Without it, the app falls back to a `MockLanguageModel` that returns static demo components — useful for development without API credits.

`JWT_SECRET` defaults to a development key if unset; set it for production.

## Architecture

UIGen is a Next.js 15 App Router app that lets users describe React components in a chat UI and see them rendered live in an iframe.

### Data flow

```
User message → /api/chat (streaming) → Claude Haiku → tool calls
    → FileSystemContext (virtual FS) → PreviewFrame (Babel + esm.sh iframe)
```

The virtual file system is entirely in-memory — no files are written to disk. `VirtualFileSystem` (`src/lib/file-system.ts`) is a plain class that the `FileSystemContext` wraps with React state. Tool calls from the AI (streamed via Vercel AI SDK) are handled in the context to mutate the virtual FS.

### Key files

| File | Role |
|------|------|
| `src/app/api/chat/route.ts` | AI endpoint — injects system prompt, defines tools, streams response |
| `src/lib/file-system.ts` | `VirtualFileSystem` class — all FS operations live here |
| `src/lib/contexts/file-system-context.tsx` | Wraps VirtualFileSystem in React state; executes tool calls |
| `src/lib/contexts/chat-context.tsx` | Vercel AI SDK integration; tracks anonymous session work |
| `src/components/preview/PreviewFrame.tsx` | Transpiles virtual FS files with `@babel/standalone`, builds an import map using esm.sh, injects into `iframe srcdoc` |
| `src/lib/provider.ts` | Returns the real Anthropic model or `MockLanguageModel` |
| `src/lib/prompts/` | System prompt for component generation |
| `src/lib/tools/` | AI tool definitions: `str_replace_editor` and `file_manager` |

### AI tools

The API route exposes two tools to Claude:
- **`str_replace_editor`** — create files, replace content, insert lines (maps to `VirtualFileSystem` methods)
- **`file_manager`** — rename or delete files/directories

### Preview rendering

`PreviewFrame` is the most complex component. It:
1. Collects all `.tsx`/`.jsx`/`.ts`/`.js` files from the virtual FS
2. Transpiles them with Babel (standalone, in-browser)
3. Builds an ES module import map pointing to esm.sh for third-party packages
4. Writes everything into an `iframe srcdoc` blob

### Persistence

- Authenticated users: project messages and virtual FS data serialized to JSON and stored in SQLite via Prisma (`Project.messages`, `Project.data`)
- Anonymous users: state lives only in React context for the session

### Auth

JWT stored in an httpOnly cookie. Middleware protects `/api/projects/*` and `/api/filesystem/*`. The app is fully usable without auth — anonymous projects just aren't persisted.

## Testing

Tests use Vitest + jsdom. Files live in `**/__tests__/*.test.ts(x)`. The virtual FS and its context are the primary test targets. No component snapshot tests exist.
