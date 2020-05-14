# Introduction

As state government operators of election infrastructure, we believe the protection of our election infrastructure is critical to the integrity of our democracy. Therefore, we value the input of security researchers acting in good faith to help us maintain a high standard for the security of our systems, which in turn gives American voters confidence in our electoral process. This includes encouraging responsible vulnerability research and disclosure. This policy sets out our definition of good faith in the context of finding and reporting vulnerabilities, as well as what you can expect from us in return.

# Systems In Scope 

The scope of this policy includes only Internet-accessible election applications and infrastructure owned by the participating state agencies (and their county and local subdivisions), to include:
- Voter registration databases,
- e-Poll books,
- Election night reporting systems,
- *etc... [State or County completes with in-scope domains and system types/categories].*

Any systems not listed above are out-of-scope for security testing under this policy. Any discovered or suspected vulnerabilities in out of scope systems should be reported to the appropriate vendor, or to CERT/CC.

# Systems Out of Scope 

Out-of-scope systems include infrastructure or other equipment not owned by participating state agencies and their county and local subdivisions. It is the responsibility of vulnerability researchers, testers, or others seeking to comply with this policy to ensure the equipment or system is not out-of-scope.

*[Optional: Provide more details on systems that are out-of-scope and/or how vulnerability reporters or researchers may distinguish systems that are in- and out-of-scope.]*

# Official Communication Channels 

Information regarding vulnerabilities for in-scope systems should be sent through the following channel: *[Required: Email address, web form URL, or platform URL for vulnerability submissions goes here]*

# Expectations

When working with us according to this policy, you can expect us to:
- Always hold the integrity of the democractic process as critical to our mission;
- Prioritize security and privacy of voters and our other stakeholders;
- Work with you to understand and validate your report, including a timely initial response to the submission;
- Work to mitigate discovered vulnerabilities within our budget and operations constraints; 
- Recognize your contribution to improving our security - after mitigation and at a time of our choosing - if you are the first to report a unique vulnerability, and your report triggers a code or configuration change; and
- Extend Safe Harbor for your vulnerability research that adheres to the Ground Rules.

While we will always strongly consider your assessment and recommendations regarding vulnerability severity, we retain the authority to determine what vulnerabilities can and should be remediated and in what time frame. We will always prioritize our mission to administer fair elections, and will address vulnerabilities to the best of our ability to achieve that goal.

# Ground Rules

To encourage responsible vulnerability research and to avoid any confusion between good-faith research and malicious attack, we ask that you follow these Ground Rules. Activities that do not follow these Ground Rules should be considered out of scope. Modifications to these Ground Rules can only be provided in writing from authorized officials. 

- Play by the rules. This includes following this policy, as well as any other relevant agreements. If there is any inconsistency between this policy and any other relevant terms, the terms of this policy will prevail;
- Report any vulnerability you’ve discovered promptly through the Official Channels listed above. Use only the Official Channels to discuss vulnerability information with us; Public disclosure of election-related vulnerabilities can harm voter confidence and negate the benefits of this policy, and thus is out of scope of this policy, unless permission is granted in writing by officials with authority to do so. Keep the details of any discovered vulnerabilities confidential until they are mitigated, according to the Disclosure Policy, unless permission is granted in writing by officials with authority to do so;
- Perform testing only on in-scope systems, and respect systems and activities which are out-of-scope;
- You should only interact with test accounts you own or with explicit permission from the account holder; 
- Do not damage our systems or degrade user experience, such as via a denial-of-service attack, and under no circumstances disrupt a live election or voters' ability to cast ballots;
- Do not engage in phishing attacks;
- Do not misrepresent yourself to be an election worker, government official, or representative of another organization;
- Do not exfiltrate, modify, or destroy system data;
- Avoid violating the privacy of others; do not obtain, modify, or disclose sensitive or individually identifying information of third parties; and
- Do not require payment in exchange for disclosing your findings, withholding disclosure of your findings, or other services rendered. Additional paid services, such as payment for vulnerability testing or mitigation, require a contract or arrangement separate from this policy.


If a vulnerability provides unintended access to data:
- Cease testing and submit a report immediately if you encounter any user or voter data during testing, such as Personally Identifiable Information (PII);
- Limit the amount of data you access to the minimum required for effectively demonstrating a proof of concept - for example, a screenshot of 3-5 records is sufficient for your proof of concept;
- Avoid downloading or extracting data of any kind beyond the minimum necessary for a proof of concept.

# Disclosure Policy

We have commitments both to transparency and voter trust. As part of those commitments, we seek to ensure vulnerabilities are adequately analyzed and mitigated to maintain user protection, and that public communications about vulnerabilities are accurate, helpful, and not premature. To that end, recognizing that these processes require a time commitment, and given the sensitive nature of election security and the need to preserve voter confidence in the electoral process, we request that you keep the details of any discovered vulnerabilities confidential until they are appropriately mitigated.

Until the vulnerability is mitigated, the researcher may share details of the vulnerability only with written permission from state officials with authorization to provide approval to disclose.

# Safe Harbor

When conducting vulnerability research according to this policy, we will not initiate legal action against you under the Computer Fraud and Abuse Act, the Digital Millennium Copyright Act, violations of our Terms & Conditions, or similar state laws. We will not initiate or support legal action against you for accidental, good faith violations of this policy that do not cause damage or harm or violate the privacy of others.


Please note that this safe harbor applies only to legal claims under the control of the state agencies participating in this policy. For example, the policy does not apply to third party claims that are independent of the state. You are expected to comply with all applicable laws. The state agencies participating in this policy will comply with applicable laws and lawful orders.
If at any time you have concerns or are uncertain whether your security research is consistent with this policy, please submit a report through one of our Official Channels before going any further.

# Rewards

Rewards for vulnerabilities may be awarded at the discretion of the Secretary of State as funds are available. Under this policy, security researchers are not authorized to solicit reward or payment for services rendered as part of the disclosure process.