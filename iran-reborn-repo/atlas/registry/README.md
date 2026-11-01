# Subject Registry

One CSV per Atlas part. Columns:

`id,part,type,category,jurisdiction,year,title,status,verify,source,notes`

- `id`: part letter plus four digits, e.g. `A-0001`. IDs are permanent. **Never reuse, renumber or delete an ID.** To retire a subject, set `status=withdrawn` and explain in `notes`.
- `status`: `queued` (listed only) → `drafted` → `sourced` → `published`.
- `verify`: `VERIFY` until at least one source is attached and checked.
- `year`: start year (integer) or `NNNN-NNNN` span.

Parts: A Iran timeline · B Iran laws and decrees · C Iranian state programs and institutions · D Wars, sanctions and diplomacy · E World recovery, transition and justice programs · F World laws and programs on migration, labor, environment, space, sea, religion and state, information, corruption, population.

Target: roughly 6,500 subjects across all parts (see `tools/stats.py`). New subjects are appended to the end of the relevant CSV with the next free ID.
