# Contribution Guidelines

Please format your contributions with either of the following commands:

```bash
jq --indent 3 -s '.[] | unique_by(.program_name)' < program-list.json > _ && mv _ program-list.json
```

or

```bash
./tools/format.sh
```

Alternatively, allow editing your fork by maintainers.

### Getting started

If you have new VDP or bug bounty program information to add, update, or delete in the [#diodb open-source vulnerability disclosure and bug bounty program list](https://github.com/disclose/diodb/blob/master/program-list.json), we'd love you to contribute by issuing a Pull Request.

If you're new to Github, [this article](https://help.github.com/articles/creating-a-pull-request-from-a-fork/) is a good primer on how PRs work. If you'd like to help us create tooling to allow updates without the use of Git and PRs, get in touch at hello@disclose.io.

### Adding a new program?

Programs on the bug-bounty-list need to satisfy the definition of a public bug bounty or vulnerability disclosure program, which means they need two key components:

1. `policy_url` - A publicly accessible vulnerability disclosure policy, sometimes called a program brief or bounty brief, and
2. `contact_url` - A publicly accessible intake channel for vulnerability submissions. This intake channel must be explicitly mentioned in the vulnerability disclosure policy.

If you work with an organization like this, encourage them to launch a formal and public program and point them to disclose.io for helpful tools to assist them along the way!

### Other tips

- Launch date can be tricky to find on some programs e.g., it's buried in a press release or blog post and not on the program page. If you think you've found a launch date, please include a reference to where you found it in the PR so the maintainers can check.
- Some companies will offer these things on an ad-hoc or case-by-case basis, but this doesn't mean they're committing to do it for everyone. Be careful with the `bounty_offered`, `swag_offered`, and `hall_of_fame` options. As always, read the program page.

### Some examples of suggestions that won't be accepted

Remember, the goal of The disclose.io Project is to drive the adoption of VDP with best practices, so we'll only accept entries that satisfy the Policy and Intake requirement above.  

Sometimes, organizations have informal vulnerability reporting setups. While these organizations provide lucky or persistent folks with the option to report issues, this arrangement does NOT constitute a formally established and fully endorsed public VDP.

Some examples of this include:

1. Private programs
2. Invitation-only programs
3. Updates where the intake channel is unlisted or informal in the policy
4. Programs that you heard about from a friend but aren't listed publicly
5. Programs without a public policy or a nominated channel for communication
6. security.txt entries without a valid "policy_url"