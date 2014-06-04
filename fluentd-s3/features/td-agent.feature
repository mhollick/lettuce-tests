Feature: Upload to S3
  In order to reliably upload logs to S3
  As a developer
  I want to test uploading to S3 works

  Scenario: Access to development bucket
    Given my configuration file is s3.ini
    Given my test file is called foo
    Given my test file contains foobarbaz
    When I upload my test file
    Then I can see the test file at S3: "True"


    Then I can download it and 
