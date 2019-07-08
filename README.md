# disclose.io

> Driving safety, simplicity, and standardization in vulnerability disclosure.

**disclose.io** is a collaborative and vendor-agnostic project to standardize best practices around safe harbor for good-faith security research, and expands on the work done by Bugcrowd and CipherLaw’s [Open Source Vulnerability Disclosure Framework](https://github.com/bugcrowd/disclosure-policy), Amit Elazari’s [#legalbugbounty](https://www.youtube.com/watch?v=0fMrZCcshyc), and Dropbox’s [recent blog post](https://blogs.dropbox.com/tech/2018/03/protecting-security-researchers/).

The design philosophy of the disclose.io framework is to balance four forces:

- Legal completeness,
- Safe harbor for security researchers,
- Safe harbor for program owners, and
- Readability for those who don’t have a legal background or who don’t speak English as a first language.

Organizations displaying the disclose.io logo are committing to a set of [**Core Terms**](core_terms/) focused on creating safe harbor for good-faith security research. In order to uphold this commitment, such organizations are also required to provide clear definitions regarding the permitted **Scope** for such research, one or more **Official Communication Channels**, and a formal **Disclosure Policy**.

## Requirements

In order to use disclose.io and associated logos in a security research or disclosure program, organizations must have the following items clearly defined within the context of each disclose.io compliant program:

- **Scope** – A complete list of "In-Scope" properties that the organization is explicitly allowing good-faith security researcher on, and optionally:
    - **Out-of-Scope** - A non-exhaustive list of properties and security testing activities that the organization strongly wishes to discourage testing against.
    - **Rewards** – Information on whether or not compensation will be provided for valid, unique issues, as well as the type and parameters of that compensation.
- **Official Communication Channels** – A full list of the communication methods that are made available by the organization to receive and communicate about vulnerability submissions;
- **Disclosure Policy** – A clear policy outlining the conditions under which the existence and/or details of a reported issue may be disclosed to third parties. Examples include:
    - **Coordinated Disclosure**: Vulnerability details may be shared with third parties after the vulnerability has been fixed and the program owner has provided permission to disclose or after 90 days from submission, whichever is sooner.
    - **Discretionary Disclosure**: Vulnerability details may be shared with third parties only after requesting and receiving explicit permission from the program owner.
    - **Non-Disclosure**: Vulnerability details (and the existence of the program itself if private) cannot be shared with third parties.
    
Examples of these items are provided in the [**Additional Terms**](additional_terms/) section of the disclose repo.

## Core Terms and Logo Usage

# "Full" Safe Harbor



If the above requirements are met, an organization may display the disclose.io [Core Terms](core_terms/), as well as the disclose.io logo, in conjunction with their authorized security research program's policies in order to indicate their intention to provide safe harbor for good-faith security research.

# "Partial" Safe Harbor

Organizations that have not met all of the requirements for providing full safe harbor (e.g. do not sufficiently define the terms outlined in **Requirements**) may still provide a simplified goodwill statement about not pursuing legal action related to security research that DOES NOT represent the same level of commitment that full safe harbor in accordance with the Disclose.io requirements does.

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">disclose</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://disclose.io" property="cc:attributionName" rel="cc:attributionURL">disclose.io</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
