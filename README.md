# GitHub Build Status

## Description:
This plugin enables Codefresh Pipelines to update the Build Status of a commit in GitHub Cloud or GitHub Enterprise.

Can be used to trigger pipelines for CI, Pull Request merge check etc.

## Usage

In this section will find the available Parameters and Examples.

The following examples are using the `ydemetriades/github-buildstatus` Codefresh step available in [Marketplace](https://codefresh.io/steps/step/ydemetriades%2Fgithub-buildstatus)

### Parameters

Both, Codefresh step and docker image, are configurable through parameters in order to perform the action.

|Name|Required|Description|Available Options|Default Value|
|----|--------|-----------|-----------------|-------------|
|GH_BSN_URL|No|GitHub API Url|-|https://api.github.com/|
|GH_BSN_REPO_AUTH_USER|Yes|GitHub Server API Authorization Username|-|-|
|GH_BSN_REPO_AUTH_PASSWORD|Yes|GitHub Server API Authorization Password|-|-|
|CF_BUILD_STATUS|Yes|Build Status|`error` `failure` `pending` `success`|-|
|GH_BSN_BUILD_CONTEXT|No|Build context. eg. 'codefresh/ci'|-|`default`|

### Example

```yaml
version: '1.0'
steps:
  GH_Update_BuildStatus:
    type: ydemetriades/github-buildstatus
    arguments:
      GH_BSN_REPO_AUTH_USER: ${{GH_BSN_REPO_AUTH_USER}}
      GH_BSN_REPO_AUTH_TOKEN: ${{GH_BSN_REPO_AUTH_TOKEN}}
      CF_BUILD_STATUS: 'success'
      GH_BSN_BUILD_CONTEXT: 'codefresh-build/ci'
```

### Advanced Example

```yaml
version: '1.0'
mode: parallel
steps:
  GH_Update_BuildStatus_InProgress:
    type: ydemetriades/github-buildstatus
    fail_fast: false
    arguments:
      GH_BSN_REPO_AUTH_USER: ${{GH_BSN_REPO_AUTH_USER}}
      GH_BSN_REPO_AUTH_TOKEN: ${{GH_BSN_REPO_AUTH_TOKEN}}
      CF_BUILD_STATUS: 'pending'
      GH_BSN_BUILD_CONTEXT: 'codefresh-build/ci'

    ## [Some more steps...]

    GH_Update_BuildStatus_Finished:
    type: parallel
    fail_fast: false
    when:
      condition:
        all:
          myCondition: workflow.result == 'finished'
    steps:
      GH_Update_BuildStatus_Successful:
        type: ydemetriades/github-buildstatus
        when:
          condition:
            all:
              myCondition: workflow.result == 'success'
        arguments:
          GH_BSN_REPO_AUTH_USER: ${{GH_BSN_REPO_AUTH_USER}}
          GH_BSN_REPO_AUTH_TOKEN: ${{GH_BSN_REPO_AUTH_TOKEN}}
          CF_BUILD_STATUS: 'success'
          GH_BSN_BUILD_CONTEXT: 'codefresh-build/ci'
      GH_Update_BuildStatus_Failed:
        type: ydemetriades/github-buildstatus
        when:
          condition:
            all:
              myCondition: workflow.result == 'failure'
        arguments:
          GH_BSN_REPO_AUTH_USER: ${{GH_BSN_REPO_AUTH_USER}}
          GH_BSN_REPO_AUTH_TOKEN: ${{GH_BSN_REPO_AUTH_TOKEN}}
          CF_BUILD_STATUS: 'failure'
          GH_BSN_BUILD_CONTEXT: 'codefresh-build/ci'
```

## Maintainers


[Yiannis Demetriades](https://github.com/ydemetriades)
