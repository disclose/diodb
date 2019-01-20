# disclose.io/bug-bounty-list

> The open-sourced and community-powered directory of ALL known public bug bounty and vulnerability programs, including their safe-harbor status.  

## Contributing to the list

# How-to contribute  
If you've found a new program, new information on an existing program, or think a program should be deleted, you can contribute to bug-bounty-list by issuing a pull request (PR) to the repo. If you're new to Github, [this article](https://www.thinkful.com/learn/github-pull-request-tutorial/#Time-to-Submit-Your-First-PR) is a good primer on how PRs work.  

# (READ THIS FIRST) Before you go hunting for new programs to add...

* Programs on bug-bounty-list need to satisfy the definition of a public bug bounty or vulnerability disclosure program, which means they need two key components:
1. A publicly accessible vulnerability disclosure policy (sometimes called a program brief, or bounty brief), and 
2. A publicly accessible channel for vulnerability submission **which is explicitly mentioned in the vulnerability disclosure policy**. 
* Some examples of suggestions that won't be accepted:
1. Private programs  
2. Invitation-only programs
3. Programs that you heard about from a friend but aren't listed publicly
4. Programs without a public policy or a nominated channel for communication
-- 

# Definition of fields 

program_name (required): What is the name of the company or product team responsible for the program?
policy_url (required): Where can the policy which defines the program be found? (Usually a webpage e.g. /security, a URL on a vulnerability management platform, or in a robots.txt or security.txt file)
submission_url (required): Where does policy say vulnerability submissions should be sent? (Usually a web form, a URL on a vulnerability management platform, or an email address. Emails can be added as URLs using 'mailto:')
launch_date (optional): When does the program say it was launched?
cash_reward (optional): Does the program commit to rewarding vulnerabilities?
swag (optional): Does the program commit to sending swag out for vulnerabilities?
hall_of_fame (optional): Does the program have a listing or Hall of Fame page acknowledging vulnerability reporters?
safe_harbor (required): Does the program support full or partial safe-harbor? 

Example: Tesla

~~~~
  {
    "program_name": "Tesla",
    "policy_url": "https://bugcrowd.com/tesla",
    "submission_url": "https://bugcrowd.com/tesla/report",
    "launch_date": "",
    "cash_reward": true,
    "swag": false,
    "hall_of_fame": true,
    "safe_harbor": "full"
  },
~~~~

# How to fill out the safe-harbor field

The list supports three safe-harbor states: Full, Partial, and None. The flow below will help you determine which applies to the policy as you contribute to the list:  

1. Does the policy mention anything about legal protections for good-faith hackers? If it does, go to Step 2. If not, then you should choose "None". 
2. Does the policy talk about authorization of testing and/or exemption from legal terms? If it does, you should choose "Full". If not got to Step 3.
3. Does the policy talk about "not legally pursuing researchers" or use similar language, but does not explicitly grant authorization and/or exemption for security testing? If it does, you should choose "Partial". 

# Other tips  

* Launch date can be tricky to find on some programs e.g. found in a press release or blog post, and not on the program page. If you think you've found a missing launch date, please include a reference to where you found it in the PR.
* Be careful with the cash_reward, swag, and hall_of_fame options. Some companies will offer these things on an ad-hoc or case-by-case basis, but this doesn't mean they're committing to do it for everyone. As always, read the program page.