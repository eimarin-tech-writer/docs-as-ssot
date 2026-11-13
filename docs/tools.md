# Tools: running two agents in any AI

An "agent" here means a **separate conversation**, with a file from `agents/` pasted at the start and the source attached. That's all. It works anywhere.

The exact names of features (projects, Gems, GPTs, agents) change often and differ by plan. The table below is a starting point; check what your account has.

| Tool | Generator | Verifier | Where files live |
|---|---|---|---|
| Claude | a Project with `agents/generator.md`, `spec.md`, `style-guide.md` in its knowledge | another Project or a new conversation, with only the source, the output and the criteria | in the Project |
| ChatGPT | a Project or a custom GPT | a new conversation, outside the project | in the Project |
| Gemini | a Gem with the instructions | a new conversation, without the Gem | attached to the Gem |
| Copilot | an agent or a conversation with the instructions pasted | a new conversation | attached in the conversation |

## Rules that hold everywhere

1. **Two conversations, not one.** The Generator does not see what the Verifier thinks, and the other way round.
2. **Attach the source; don't summarize it.** If you can't attach, paste it whole.
3. **The instructions are the files in `agents/`**, pasted as they are. Don't rewrite them from memory.
4. **If you use several tools, choose roles, not comparisons.** One tool generates, another verifies, in a single pass, with fixed criteria and a card at the end. If you catch yourself running the same prompt in four places and comparing, you have left the system.
5. **Work data stays in the work account.** Before you put a transcript in a personal account, check your employer's policy.

## Without Python

`check_ssot.py` is an optional layer. Without it, add this step to the Verifier's instructions: "for each row, look for the quote on the cited line and say whether it appears verbatim". A model can do this, but not deterministically, so run it twice and compare.
