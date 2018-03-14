# sfdx-simplesalesforce

This repository demonstrates how to use Salesforce DX and scratch orgs to perform integration testing in the CI flow for an off-platform tool that integrates to Salesforce.

Specifically, it shows how to use Salesforce DX to create a scratch org and acquire credentials (either username and password or access token and instance URL) for that scratch org, and then "test" a mock Python tool that uses `simple_salesforce` to connect to the Salesforce API. We first place the relevant credential values in environment variables (as may be required by some tools), and then pass them via the command line.

The CI build also uses Salesforce DX to perform a Metadata API deploy that installs a global IP whitelist, which obviates the need for a security token while logging in with a username and password. SFDX will likely [never support](https://success.salesforce.com/_ui/core/chatter/groups/GroupProfilePage?g=0F93A000000HTp1SAG&fId=0D53A00003EtYb9SAF) generating and returning the user's security token, so an empty string ("") can be used with `simple_salesforce` in the username and password login style once these security settings have been deployed.