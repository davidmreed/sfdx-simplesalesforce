import argparse
import simple_salesforce

a = argparse.ArgumentParser()

a.add_argument('-u', '--username', dest='user', default=None)
a.add_argument('-p', '--password', dest='password', default=None)
a.add_argument('-t', '--security-token', dest='token', default=None)
a.add_argument('-a', '--access-token', dest='access_token', default=None)
a.add_argument('-i', '--instance-url', dest='instance_url', default=None)
a.add_argument('-s', '--sandbox', dest='sandbox', action="store_true")

args = a.parse_args()

if None not in [args.access_token, args.instance_url]:
    connection = simple_salesforce.Salesforce(instance_url=args.instance_url, session_id=args.access_token)
elif None not in [args.username, args.password, args.token]:
    connection = simple_salesforce.Salesforce(username=args.user, 
                                              password=args.password, 
                                              security_token=args.token, 
                                              sandbox=args.sandbox)

assert connection is not None

results = connection.query('SELECT Id FROM Account')

assert results is not None