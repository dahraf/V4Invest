# Data governance and public repository policy

Public repository means public code, not public user data or automatic rights to republish information. No actual holdings, brokerage exports, credentials, private collection links, user identifiers, or raw restricted provider data in Git. Public profile links can be research candidates; do not include the identity or URL of anyone's private saved collection.

## Rights and privacy gate

For each source record the current terms URL, review date, reviewer, permitted retrieval method, rate restrictions, retention, permitted AI processing, commercial use and redistribution. Unknown is not approval. Public accessibility alone is not authorization for bulk collection, reuse, transcription or training. Link and cite rather than copy when rights are unclear; honor source requirements, corrections and deletion obligations. No automated Instagram/Telegram ingestion until platform and content rights are confirmed. Use authorized imports and partnerships where feasible.

## Data classes

- Public code and synthetic test fixtures: allowed in repo after review.
- Public source metadata and links: allowed when not revealing personal information.
- Licensed/restricted content: isolated from Git, use only within applicable permission.
- Personal portfolios and brokerage data: private workspace only; explicitly authorized import, least privilege, encrypted storage, deletion/export controls.
- Secrets/tokens: environment or secret manager, never commit or log.

## Pre-publication checklist

Review archive contents and Git history, `.gitignore`, fixtures, logs, example configurations, credential scans and dependency licenses. A `.gitignore` alone is not a security boundary. Do not publish an actual database. Select a code license explicitly (Apache-2.0 suggested for broad reuse; AGPL-3.0 alternative if network copyleft desired). Public code without an approved license must not be described as licensed open source. Review Iranian financial-advice regulations and provider licenses before public recommendations or monetization. No automated trading.
