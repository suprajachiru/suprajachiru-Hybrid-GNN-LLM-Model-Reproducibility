# Dataset acquisition

Raw datasets are not bundled. Record the exact version, retrieval date, source terms, label semantics, and checksums in your experiment logs.

- **YelpCHI:** https://doi.org/10.57760/sciencedb.17088 — use the provider's authorized download route; the DOI landing page may not be a direct archive URL.
- **FakeNewsNet:** https://github.com/KaiDMML/FakeNewsNet — the official repository notes that complete data cannot be redistributed as a single package because of platform privacy policies and publisher copyright. Follow source restrictions.
- **Amazon Reviews’23:** https://amazon-reviews-2023.github.io/ — raw All Beauty reviews may be accessible through Hugging Face dataset tooling. Raw records do not inherently provide verified fake/genuine labels for every item. Do not invent labels from ratings without a defensible, documented protocol.

Manuscript Table 4 reports 67,395 YelpCHI instances, 23,196 FakeNewsNet instances, and 701,528 Amazon Reviews’23 (All Beauty) instances. These are manuscript-reported counts; downloaded/filtered counts may differ. Verify row counts and label mapping before comparing metrics.
