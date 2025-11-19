> # Summary
> 
>     * Adds `halodoc bugbounty program` to the DIODB.
> 
>     * Performed `jq --indent 3 -s '.[] | unique_by(.program_name)' < program-list.json > _ && mv _ program-list.json` on the program database which resulted in `raidboxes.io` being corrected in positioning as well.
> 
> 
> # Quality Assurance Checklist
> 
> < Confirmation of this pull request meeting the following requirements, prior to merge >
> Review Items 	Y/N
> Site has a publicly known bug bounty or vulnerability disclosure program 	Y
> Disclosure policy is publicly available 	Y
> Public URL 	Y
> Submission follows the [Diodb schema](https://github.com/disclose/diodb/blob/master/program-list-schema.json) 	Y
> 
> Your Twitter handle (Optional): 
