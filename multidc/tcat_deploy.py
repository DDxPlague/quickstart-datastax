#!/usr/bin/env python
# authors:
# avattathil@gmail.com
# License Apaache 2.0
#
# Purpose: This program (tcat) is a caloudformation testing tool
# Tests can defined in a configuration yaml (config.yml)


from taskcat import TaskCat
import yaml

def main():
    tcat_obj = TaskCat()
    tcat_obj.welcome('taskcat.io')
    # Initalize cli interface
    args = tcat_obj.interface
    # Init aws api and set default auth method
    tcat_obj.set_config(args.config_yml)
    # Get API Handle - Try all know auth
    tcat_obj.aws_api_init(args)

# Run in ymal mode (Batch Test execution)
# --Begin
# Check for valid ymal and required keys in config
    if args.config_yml is not None:
        print "[TSKCAT] : Mode of operation: \t [ymal-mode]"
        print "[TSKCAT] : Configuration yml: \t [%s]" % args.config_yml

        test_list = tcat_obj.validate_yaml(args.config_yml)

# Load ymal into local tcat config
        with open(tcat_obj.get_config(), 'r') as cfg:
            tcat_cfg = yaml.safe_load(cfg.read())
        cfg.close()

        tcat_obj.s3upload(tcat_cfg)
        tcat_obj.validate_template(tcat_cfg, test_list)
        tcat_obj.validate_parameters(tcat_cfg, test_list)
        stackinfo = tcat_obj.stackcreate(tcat_cfg, test_list, 'quickstart-dse)
        tcat_obj.get_stackstatus(stackinfo , 5)

# --End
# Finish run in ymal mode

main()
