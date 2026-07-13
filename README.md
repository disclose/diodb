<div align="center">

<a href="https://disclose.io"><img src="docs/marquee.png" alt="diodb · disclose.io" width="820"></a>

# diodb

### The community database of every **VDP &amp; bug-bounty program** and its safe-harbor status — now served live at [directory.disclose.io](https://directory.disclose.io).

<p>
<a href="LICENSE"><img src="https://img.shields.io/github/license/disclose/diodb?color=5B3AB6&label=license" alt="license"></a>
<a href="https://directory.disclose.io"><img src="https://img.shields.io/badge/live-directory.disclose.io-5B3AB6" alt="live directory.disclose.io"></a>
<a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/contributions-welcome-5B3AB6" alt="contributions welcome"></a>
</p>

*Part of **[the disclose.io Project](https://disclose.io)** — the open, vendor-neutral infrastructure for vulnerability disclosure. [Browse the ecosystem →](https://github.com/disclose)*

</div>

---

> [!NOTE]
> ### diodb is the open dataset. [directory.disclose.io](https://directory.disclose.io) is the live front-end.
> The directory is the searchable, always-current place to **look programs up**. This repo is the open, version-controlled, CC0 dataset behind that story — and it remains **open to contributions**.
>
> If you just want to find a program, use the [directory](https://directory.disclose.io). If you want to add or correct one in the open dataset, **pull requests here are welcome** — see [How to Contribute](#how-to-contribute).


## About this dataset

### Quick links

|Purpose|Link|
|-|-|
| Search through the database front-end  | [https://disclose.io/programs](https://disclose.io/programs)  |
| Download the raw database in .json format  | [https://github.com/disclose/diodb/raw/master/program-list.json](https://github.com/disclose/diodb/raw/master/program-list.json)  |
| Generate your own Vulnerability Disclosure Program | [https://policymaker.disclose.io/](https://policymaker.disclose.io/) |
| Join disclose.io Community Forum  | [https://community.disclose.io](https://community.disclose.io) |
| Learn more about Vulnerability Disclosure Programs (VDP) | [https://github.com/disclose/dioterms](https://github.com/disclose/dioterms) |

### Why does diodb exist?

diodb exists to drive the adoption of Safe Harbor for hackers and promote the cybersecurity posture of early adopters, simplify the process of finding the right contacts and channel at an organization, and help both finders and vendors align around the expectations of engagement. It also provides a simple, vendor-agnostic point of engagement for program operators, potential program operators, and the security community to maintain updates to their program. 

## How to Contribute

Pull requests are welcome. To add or update a program in the open dataset:

1. Edit `program-list.json`.
2. **Format and sort the file** — CI enforces this, and it is the single most common reason a PR goes red:
   ```sh
   jq --indent 3 -s '.[] | unique_by(.program_name)' < program-list.json > _ && mv _ program-list.json
   ```
3. Open a PR. CI will validate the JSON, check for duplicates, and verify the links.

Full guidelines are in [CONTRIBUTING.md](CONTRIBUTING.md).

Prefer not to use git? You can also:

- **Look a program up** → [directory.disclose.io](https://directory.disclose.io)
- **Ask a question or discuss** → [community.disclose.io](https://community.disclose.io)

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">disclose</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://disclose.io" property="cc:attributionName" rel="cc:attributionURL">disclose.io</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
