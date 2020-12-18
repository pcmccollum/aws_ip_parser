#!/usr/bin/env python3
'''
Amazon Public IP Parser
'''

import json, argparse, urllib.request, validators

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Does stuff with Amazon public JSON data")
    parser.add_argument("-u", "--url", required=True, help="AWS JSON URL")
    parser.add_argument("-r", "--region", required=True, help="AWS region from which to pull data")
    args = parser.parse_args()
    print(args)
    if validators.url(args.url):
        print("Good choice! Now let's make sure there is JSON data here...")
        with urllib.request.urlopen(args.url) as url:
            try:
                myjson = json.loads(url.read().decode())
                print("Alright! Found some! Now validating the region:\n")
                for prefix in myjson["prefixes"]:
                    if prefix["region"] == args.region:
                        print("CIDR: {}".format(prefix["ip_prefix"]))
                        print("Service: {}".format(prefix["service"]))
                        print("Region: {}".format(prefix["region"]))
            except:
                print("Whoops! No JSON data.")
                   
    else:
        print("Whoops. You done messed up.")
