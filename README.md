# The disclose.io Database (diodb)

A true, community-powered, vendor agnostic directory of all known VDP and BBPs, contact details, policy location, preferred languages, and the status of:

- Safeharbor
- Availability rewards, hall of fame, swag
- Disclosure policy

## Quickly search the database online: [https://disclose.io/programs/](https://disclose.io/programs/)

## View the database raw: [https://github.com/disclose/diodb](https://github.com/disclose/diodb)

## Visit this project on GitHub: [https://github.com/disclose/diodb](https://github.com/disclose/diodb)

[![Disclose.io Vulnerability, VDP, and Bug Bounty Program Database](diodb-hero-image.png?raw=true "Disclose.io Vulnerability, VDP, and Bug Bounty Program Database")](https://github.com/disclose/diodb)

### Quick Links

|Purpose|Link|
|-|-|
| Search through the database front-end  | [https://disclose.io/programs](https://disclose.io/programs)  |
| Download the raw database in .json format  | [https://github.com/disclose/diodb/raw/master/program-list.json](https://github.com/disclose/diodb/raw/master/program-list.json)  |
| Generate your own Vulnerability Disclosure Program | [https://policymaker.disclose.io/](https://policymaker.disclose.io/) |
| Join disclose.io Community Forum  | [https://community.disclose.io](https://community.disclose.io) |
| Learn more about Vulnerability Disclosure Programs (VDP) | [https://github.com/disclose/dioterms](https://github.com/disclose/dioterms) |

### Why does diodb exist?

diodb exists to drive the adoption of Safe Harbor for hackers and promote the cybersecurity posture of early adopters, simplify the process of finding the right contacts and channel at an organization, and help both finders and vendors align around the expectations of engagement. It also provides a simple, vendor-agnostic point of engagement for program operators, potential program operators, and the security community to maintain updates to their program. 

## How to contribute

Please format your contributions using `jq`, or allow editing forks by maintainers :)

```bash
jq --indent 3 -s '.[] | unique_by(.program_name)' < program-list.json > _ && mv _ program-list.json
```

or

```bash
./tools/format.sh
```

### Getting started

If you have new VDP or bug bounty program information to add, update, or delete in the [#diodb open-source vulnerability disclosure and bug bounty program list](https://github.com/disclose/diodb/blob/master/program-list.json), we'd love you to contribute by issuing a Pull Request.

If you're new to Github, [this article](https://help.github.com/articles/creating-a-pull-request-from-a-fork/) is a good primer on how PRs work. If you'd like to help us create tooling to allow updates without the use of Git and PRs, get in touch at hello@disclose.io.

### Adding a new program?

Programs on the bug-bounty-list need to satisfy the definition of a public bug bounty or vulnerability disclosure program, which means they need two key components:

1. "policy_url" - A publicly accessible vulnerability disclosure policy, sometimes called a program brief or bounty brief, and
2. "contact_url" - A publicly accessible intake channel for vulnerability submissions. This intake channel must be explicitly mentioned in the vulnerability disclosure policy.

If you work with an organization like this, encourage them to launch a formal and public program and point them to disclose.io for helpful tools to assist them along the way!

### Other tips

* Launch date can be tricky to find on some programs e.g., it's buried in a press release or blog post and not on the program page. If you think you've found a launch date, please include a reference to where you found it in the PR so the maintainers can check.
* Some companies will offer these things on an ad-hoc or case-by-case basis, but this doesn't mean they're committing to do it for everyone. Be careful with the "bounty_offered", "swag_offered", and "hall_of_fame" options. As always, read the program page.

### Some examples of suggestions that won't be accepted:

Remember, the goal of The disclose.io Project is to drive the adoption of VDP with best practices, so we'll only accept entries that satisfy the Policy and Intake requirement above.  

Sometimes, organizations have informal vulnerability reporting setups. While these organizations provide lucky or persistent folks with the option to report issues, this arrangement does NOT constitute a formally established and fully endorsed public VDP.

Some examples of this include:

1. Private programs
2. Invitation-only programs
3. Updates where the intake channel is unlisted or informal in the policy
4. Programs that you heard about from a friend but aren't listed publicly
5. Programs without a public policy or a nominated channel for communication
6. security.txt entries without a valid "policy_url"

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">disclose</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://disclose.io" property="cc:attributionName" rel="cc:attributionURL">disclose.io</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## Other tips  

* Launch date can be tricky to find on some programs e.g. it's buried in a press release or blog post and not on the program page. If you think you've found a launch date, please include a reference to where you found it in the PR so the maintainers can check.
* Some companies will offer these things on an ad-hoc or case-by-case basis, but this doesn't mean they're committing to do it for everyone. Be careful with the bug_bounty, swag, and hall_of_fame options. As always, read the program page.
