Feature: Upload to S3
  In order to reliably upload logs to S3
  As a DevOps dude
  I want to test that my fluentd infrastructure successfully logs to S3

  Scenario: Write access to my bucket
    Given my configuration file is "../../lettuce.ini"
    Given my test file is called "foo"
    Given my test file contains "foobarbaz"
    When I upload my test file success is: "True"
    Then I can see the test file at S3 is: "True"

  Scenario: Download test file from my bucket
    Given my configuration file is "../../lettuce.ini"
    Given my test file is called "foo"
    Given my test file contains "foobarbaz"
    When I upload my test file success is: "True"
    When I download it again success is: "True"
    Then there is no difference between the files: "True"

  Scenario: Upload test log data to my bucket using fluentd
    Given my configuration file is "../../lettuce.ini"
    Given I have installed "td-agent"
    Given I have installed "td-plugin-s3"
    Given I ensure that any conflicting log at S3 is deleted first
    Given my fluentd configuration file is at "../../td-agent.conf"
    Given I wish to send "100" lines of log data at "1" line per second
    Given I wait for "5" minutes before continuing
    When I start fluentd there is no error: "True"
    When I send log data to fluentd there is no error: "True"
    When I look a s3 there is a log file there: "True"
    When I kill fluentd it dies: "True"
  
  Scenario: Varify uploaded test log data
    Given my configuration file is "../../lettuce.ini"
    Given I have installed "td-agent"
    Given I have installed "td-plugin-s3"
    Given I ensure that any conflicting log at S3 is deleted first
    Given my fluentd configuration file is at "../../td-agent.conf"
    Given I wish to send "100" lines of log data at "1" line per second
    Given I wait for "5" minutes before continuing
    When I start fluentd there is no error: "True"
    When I send log data to fluentd there is no error: "True"
    When I check local logs I have an unvarified copy of the log data: "True"
    When I look a s3 there is a log file there: "True"
    When I try to download it I succeed: "True"
    When I compare it to my local copy they are the same: "True"
    When I kill fluentd it dies: "True"

