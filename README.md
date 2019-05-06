# Rotapopulator

Designed to create a CSV file that will allow DCO's to auto generate oncall for their shift pattern based on 4 on 4 off.



# Versions

1.0 : Code clean up and initial project

1.2: Removed clutter csv file to make it easier to import

2.0: Implementation of the config file to save information

2.1: Full automation in config, daylight saving times option in config enabled.

3.0: Allow multiple staff to rota days/night when you have more then one person working the same shift.

3.1: Updated hours now that we're on GMT time.

3.1b: Implemented wrong times to start, have corrected this.

# Future versions

4.0: Making class, making shift patterns

#How the script works
You must have python3 to run the script or you can use the binary version:
* Run the script in python3
* The script will check if you have a config file
  * If the config file doesn't exist it will start a manual version of the script and save a config after
  * If a config exists it will run the automated version and you just need to select the order of users

Non automated version:
* Select the date on when you want the csv file to start populating
* Type in 4 or 8 users to work the rota you can delete a user if you make a mistake
* Type in the order the user starts their shift from
* Generates a csv file
* Check the file and if all is well import into oncall site
* !!!! PROFIT

Automated version:
* Make sure your config is filled out.
* Generates a csv file
* Check the file and if all is well import into oncall site
* !!!! PROFIT

* Binaries for all versions on Windows and Linux are available on release section.

#How to use config

* Open up the config file and you'll see a list of users to add.
* Type the username in the order on how shift starts i.e. firstnight = johnblaze
* If they're shifts that don't have two people working simply leave the _second blank and the script will populate the csv accordingly.
* Choose your date on when you want the config to start i.e. oncalldate = 2017/12/05
* Put yes or no for american daylight savings time.
* Save the file and rename it to main.cfg
* Run python or the programme and it will detect the config.

