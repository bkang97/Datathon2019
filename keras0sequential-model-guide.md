





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-4bmhxCob3U2WoK8HVl7UacoDdNejo+50BlGN9SdGtjXbsCQwp7uLtntLkL9a9CmgLPZ8L9lsOZL0ieINT9yHeA==" rel="stylesheet" href="https://github.githubassets.com/assets/frameworks-2fd1891c9e6292401a1a3de8bc3f747f.css" />
  
    <link crossorigin="anonymous" media="all" integrity="sha512-cK5dmbRZaqw0tWOJJx/cJUjbSz0kLC+skyb7Fk/BxV5rwEKjxsy0jKgajdbKyco78S7ww/EX6QFY0Pyc4Iv6xA==" rel="stylesheet" href="https://github.githubassets.com/assets/github-532e3474a82777f5619fad79f6e9e62a.css" />
    
    
    
    

  <meta name="viewport" content="width=device-width">
  
  <title>keras/sequential-model-guide.md at master · keras-team/keras</title>
    <meta name="description" content="Deep Learning for humans. Contribute to keras-team/keras development by creating an account on GitHub.">
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    <meta name="twitter:image:src" content="https://avatars0.githubusercontent.com/u/34455048?s=400&amp;v=4" /><meta name="twitter:site" content="@github" /><meta name="twitter:card" content="summary" /><meta name="twitter:title" content="keras-team/keras" /><meta name="twitter:description" content="Deep Learning for humans. Contribute to keras-team/keras development by creating an account on GitHub." />
    <meta property="og:image" content="https://avatars0.githubusercontent.com/u/34455048?s=400&amp;v=4" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="keras-team/keras" /><meta property="og:url" content="https://github.com/keras-team/keras" /><meta property="og:description" content="Deep Learning for humans. Contribute to keras-team/keras development by creating an account on GitHub." />

  <link rel="assets" href="https://github.githubassets.com/">
  <link rel="web-socket" href="wss://live.github.com/_sockets/VjI6NDU3MjE4NTM5OjI0MzFjMDEzZTgxZTJjOTUxNWRlMDIwMjhkZWZhYzg3MWJiNWUyM2M0ZmZlMDkyMGY0NDE5ZTgxODFiYzUyMmU=--f8f3a27404e8a4ae48339a1c3125173907266a35">
  <link rel="sudo-modal" href="/sessions/sudo_modal">
  <meta name="request-id" content="C15B:6E33:A84D14:1370F0C:5DAFEAFA" data-pjax-transient>


  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

      <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
    <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

  <meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-request_id" content="C15B:6E33:A84D14:1370F0C:5DAFEAFA" /><meta name="octolytics-dimension-region_edge" content="iad" /><meta name="octolytics-dimension-region_render" content="iad" /><meta name="octolytics-dimension-ga_id" content="" class="js-octo-ga-id" /><meta name="octolytics-dimension-visitor_id" content="1078302681406641509" /><meta name="octolytics-actor-id" content="16846337" /><meta name="octolytics-actor-login" content="bkang97" /><meta name="octolytics-actor-hash" content="baab070faf2fa11de37d91923c7499df390aa96d54771424f80b1076a72af5b8" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />



    <meta name="google-analytics" content="UA-3769691-2">

  <meta class="js-ga-set" name="userId" content="d41442a27a08e3d87b4f2fa59c6192df">

<meta class="js-ga-set" name="dimension1" content="Logged In">



  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="bkang97">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="YzZkMzk0NGE2Njg5YWU0Mzg2YTQ2NzJjZjViZDNmNjdmYzJhYjlhMzc2ZDcxMjljOGFjMzViMjcyNWI2ZjUwYnx7InJlbW90ZV9hZGRyZXNzIjoiNjguMTc1LjE0Ni4yNDciLCJyZXF1ZXN0X2lkIjoiQzE1Qjo2RTMzOkE4NEQxNDoxMzcwRjBDOjVEQUZFQUZBIiwidGltZXN0YW1wIjoxNTcxODEwMDU1LCJob3N0IjoiZ2l0aHViLmNvbSJ9">

    <meta name="enabled-features" content="ACTIONS_V2_ON_MARKETPLACE,MARKETPLACE_FEATURED_BLOG_POSTS,MARKETPLACE_INVOICED_BILLING,MARKETPLACE_SOCIAL_PROOF_CUSTOMERS,MARKETPLACE_TRENDING_SOCIAL_PROOF,MARKETPLACE_RECOMMENDATIONS,MARKETPLACE_PENDING_INSTALLATIONS,NOTIFY_ON_BLOCK,RELATED_ISSUES,GHE_CLOUD_TRIAL">

  <meta name="html-safe-nonce" content="edfa127c047267acb094a6db578f179d8131aae5">

  <meta http-equiv="x-pjax-version" content="7f62f264a995c2bd08c25afe97054c8a">
  

      <link href="https://github.com/keras-team/keras/commits/master.atom" rel="alternate" title="Recent Commits to keras:master" type="application/atom+xml">

  <meta name="go-import" content="github.com/keras-team/keras git https://github.com/keras-team/keras.git">

  <meta name="octolytics-dimension-user_id" content="34455048" /><meta name="octolytics-dimension-user_login" content="keras-team" /><meta name="octolytics-dimension-repository_id" content="33015583" /><meta name="octolytics-dimension-repository_nwo" content="keras-team/keras" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="33015583" /><meta name="octolytics-dimension-repository_network_root_nwo" content="keras-team/keras" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="false" />


    <link rel="canonical" href="https://github.com/keras-team/keras/blob/master/docs/templates/getting-started/sequential-model-guide.md" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://github.githubassets.com/favicon.ico">

<meta name="theme-color" content="#1e2327">



  <meta name="webauthn-auth-enabled" content="true">

  <meta name="webauthn-registration-enabled" content="true">

  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-in env-production emoji-size-boost page-responsive page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="p-3 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
    <span class="Progress progress-pjax-loader position-fixed width-full js-pjax-loader-bar">
      <span class="progress-pjax-loader-bar top-0 left-0" style="width: 0%;"></span>
    </span>

    
    
    


          <header class="Header js-details-container Details flex-wrap flex-lg-nowrap p-responsive" role="banner">

    <div class="Header-item d-none d-lg-flex">
      <a class="Header-link" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <svg class="octicon octicon-mark-github v-align-middle" height="32" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
</a>

    </div>

    <div class="Header-item d-lg-none">
      <button class="Header-link btn-link js-details-target" type="button" aria-label="Toggle navigation" aria-expanded="false">
        <svg height="24" class="octicon octicon-three-bars" viewBox="0 0 12 16" version="1.1" width="18" aria-hidden="true"><path fill-rule="evenodd" d="M11.41 9H.59C0 9 0 8.59 0 8c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zm0-4H.59C0 5 0 4.59 0 4c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zM.59 11H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1H.59C0 13 0 12.59 0 12c0-.59 0-1 .59-1z"/></svg>
      </button>
    </div>

    <div class="Header-item Header-item--full flex-column flex-lg-row width-full flex-order-2 flex-lg-order-none mr-0 mr-lg-3 mt-3 mt-lg-0 Details-content--hidden">
        <div class="header-search flex-self-stretch flex-lg-self-auto mr-0 mr-lg-3 mb-3 mb-lg-0 scoped-search site-scoped-search js-site-search position-relative js-jump-to"
  role="combobox"
  aria-owns="jump-to-results"
  aria-label="Search or jump to"
  aria-haspopup="listbox"
  aria-expanded="false"
>
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" role="search" aria-label="Site" data-scope-type="Repository" data-scope-id="33015583" data-scoped-search-url="/keras-team/keras/search" data-unscoped-search-url="/search" action="/keras-team/keras/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
      <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">
        <input type="text"
          class="form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable"
          data-hotkey="s,/"
          name="q"
          value=""
          placeholder="Search or jump to…"
          data-unscoped-placeholder="Search or jump to…"
          data-scoped-placeholder="Search or jump to…"
          autocapitalize="off"
          aria-autocomplete="list"
          aria-controls="jump-to-results"
          aria-label="Search or jump to…"
          data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations#csrf-token=irh9CaDU18LQyr1PQCYIv02gbcP5VUC6oNLebGkc8TkWXhU+jTvM4798ZsJOe9sBzBHWkK0h5Dbzu94lHll66Q=="
          spellcheck="false"
          autocomplete="off"
          >
          <input type="hidden" class="js-site-search-type-field" name="type" >
            <img src="https://github.githubassets.com/images/search-key-slash.svg" alt="" class="mr-2 header-search-key-slash">

            <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
              
<ul class="d-none js-jump-to-suggestions-template-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 00-1 1v14a1 1 0 001 1h13a1 1 0 001-1V1a1 1 0 00-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0013 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 000-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

</ul>

<ul class="d-none js-jump-to-no-results-template-container">
  <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2">
    <span class="text-gray">No suggested jump to results</span>
  </li>
</ul>

<ul id="jump-to-results" role="listbox" class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 00-1 1v14a1 1 0 001 1h13a1 1 0 001-1V1a1 1 0 00-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0013 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 000-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 00-1 1v14a1 1 0 001 1h13a1 1 0 001-1V1a1 1 0 00-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0013 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 000-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>


    <li class="d-flex flex-justify-center flex-items-center p-0 f5 js-jump-to-suggestion">
      <img src="https://github.githubassets.com/images/spinners/octocat-spinner-128.gif" alt="Octocat Spinner Icon" class="m-2" width="28">
    </li>
</ul>

            </div>
      </label>
</form>  </div>
</div>


      <nav class="d-flex flex-column flex-lg-row flex-self-stretch flex-lg-self-auto" aria-label="Global">
    <a class="Header-link d-block d-lg-none py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15" data-ga-click="Header, click, Nav menu - item:dashboard:user" aria-label="Dashboard" href="/dashboard">
      Dashboard
</a>
  <a class="js-selected-navigation-item Header-link  mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15" data-hotkey="g p" data-ga-click="Header, click, Nav menu - item:pulls context:user" aria-label="Pull requests you created" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls" href="/pulls">
    Pull requests
</a>
  <a class="js-selected-navigation-item Header-link  mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15" data-hotkey="g i" data-ga-click="Header, click, Nav menu - item:issues context:user" aria-label="Issues you created" data-selected-links="/issues /issues/assigned /issues/mentioned /issues" href="/issues">
    Issues
</a>
    <div class="mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15">
      <a class="js-selected-navigation-item Header-link" data-ga-click="Header, click, Nav menu - item:marketplace context:user" data-octo-click="marketplace_click" data-octo-dimensions="location:nav_bar" data-selected-links=" /marketplace" href="/marketplace">
        Marketplace
</a>      

    </div>

  <a class="js-selected-navigation-item Header-link  mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore" href="/explore">
    Explore
</a>


    <a class="Header-link d-block d-lg-none mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15" href="https://github.com/bkang97">
      <img class="avatar" height="20" width="20" alt="@bkang97" src="https://avatars0.githubusercontent.com/u/16846337?s=60&amp;v=4" />
      bkang97
</a>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form action="/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="qHPkXCFOFtmNrbxrdPLty3NM+Q3k6vrTfXD8nWQ1YzqLAcBXN2ldbwvPRVP9iscs8qfQ58BuiHOrppBaLgqnMA==" />
      <button type="submit" class="Header-link mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15 d-lg-none btn-link d-block width-full text-left" data-ga-click="Header, sign out, icon:logout" style="padding-left: 2px;">
        <svg class="octicon octicon-sign-out v-align-middle" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 9V7H8V5h4V3l4 3-4 3zm-2 3H6V3L2 1h8v3h1V1c0-.55-.45-1-1-1H1C.45 0 0 .45 0 1v11.38c0 .39.22.73.55.91L6 16.01V13h4c.55 0 1-.45 1-1V8h-1v4z"/></svg>
        Sign out
      </button>
</form></nav>

    </div>

    <div class="Header-item Header-item--full flex-justify-center d-lg-none position-relative">
      <div class="css-truncate css-truncate-target width-fit position-absolute left-0 right-0 text-center">
              <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
    <a class="Header-link" href="/keras-team">keras-team</a>
    /
    <a class="Header-link" href="/keras-team/keras">keras</a>

</div>
    </div>


    <div class="Header-item mr-0 mr-lg-3 flex-order-1 flex-lg-order-none">
      

    <a aria-label="You have no unread notifications" class="Header-link notification-indicator position-relative tooltipped tooltipped-s js-socket-channel js-notification-indicator" data-hotkey="g n" data-ga-click="Header, go to notifications, icon:read" data-channel="notification-changed:16846337" href="/notifications">
        <span class="mail-status "></span>
        <svg class="octicon octicon-bell" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 12v1H0v-1l.73-.58c.77-.77.81-2.55 1.19-4.42C2.69 3.23 6 2 6 2c0-.55.45-1 1-1s1 .45 1 1c0 0 3.39 1.23 4.16 5 .38 1.88.42 3.66 1.19 4.42l.66.58H14zm-7 4c1.11 0 2-.89 2-2H5c0 1.11.89 2 2 2z"/></svg>
</a>
    </div>


    <div class="Header-item position-relative d-none d-lg-flex">
      <details class="details-overlay details-reset">
  <summary class="Header-link"
      aria-label="Create new…"
      data-ga-click="Header, create new, icon:add">
    <svg class="octicon octicon-plus" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 9H7v5H5V9H0V7h5V2h2v5h5v2z"/></svg> <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="dropdown-menu dropdown-menu-sw">
    
<a role="menuitem" class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a role="menuitem" class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a role="menuitem" class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a role="menuitem" class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>


  <div role="none" class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="keras-team/keras">This repository</span>
  </div>
    <a role="menuitem" class="dropdown-item" href="/keras-team/keras/issues/new/choose" data-ga-click="Header, create new issue" data-skip-pjax>
      New issue
    </a>


  </details-menu>
</details>

    </div>

    <div class="Header-item position-relative mr-0 d-none d-lg-flex">
      
<details class="details-overlay details-reset">
  <summary class="Header-link"
    aria-label="View profile and more"
    data-ga-click="Header, show menu, icon:avatar">
    <img alt="@bkang97" class="avatar" src="https://avatars3.githubusercontent.com/u/16846337?s=40&amp;v=4" height="20" width="20">
    <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="dropdown-menu dropdown-menu-sw mt-2" style="width: 180px">
    <div class="header-nav-current-user css-truncate"><a role="menuitem" class="no-underline user-profile-link px-3 pt-2 pb-2 mb-n2 mt-n1 d-block" href="/bkang97" data-ga-click="Header, go to profile, text:Signed in as">Signed in as <strong class="css-truncate-target">bkang97</strong></a></div>
    <div role="none" class="dropdown-divider"></div>

      <div class="pl-3 pr-3 f6 user-status-container js-user-status-context pb-1" data-url="/users/status?compact=1&amp;link_mentions=0&amp;truncate=1">
        
<div class="js-user-status-container
    user-status-compact rounded-1 px-2 py-1 mt-2
    border
  " data-team-hovercards-enabled>
  <details class="js-user-status-details details-reset details-overlay details-overlay-dark">
    <summary class="btn-link btn-block link-gray no-underline js-toggle-user-status-edit toggle-user-status-edit "
      role="menuitem" data-hydro-click="{&quot;event_type&quot;:&quot;user_profile.click&quot;,&quot;payload&quot;:{&quot;profile_user_id&quot;:34455048,&quot;target&quot;:&quot;EDIT_USER_STATUS&quot;,&quot;user_id&quot;:16846337,&quot;client_id&quot;:&quot;251061907.1570248037&quot;,&quot;originating_request_id&quot;:&quot;C15B:6E33:A84D14:1370F0C:5DAFEAFA&quot;,&quot;originating_url&quot;:&quot;https://github.com/keras-team/keras/blob/master/docs/templates/getting-started/sequential-model-guide.md&quot;,&quot;referrer&quot;:&quot;https://github.com/keras-team/keras/tree/master/docs/templates/getting-started&quot;}}" data-hydro-click-hmac="e0e5689d63fa0a3b9368cad069f8f8fa2b5ec262d87071b5ba1c4753600d7c6d">
      <div class="d-flex">
        <div class="f6 lh-condensed user-status-header
          d-inline-block v-align-middle
            user-status-emoji-only-header circle
            pr-2
"
            style="max-width: 29px"
          >
          <div class="user-status-emoji-container flex-shrink-0 mr-1 mt-1 lh-condensed-ultra v-align-bottom" style="">
            <svg class="octicon octicon-smiley" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8s3.58 8 8 8 8-3.58 8-8-3.58-8-8-8zm4.81 12.81a6.72 6.72 0 01-2.17 1.45c-.83.36-1.72.53-2.64.53-.92 0-1.81-.17-2.64-.53-.81-.34-1.55-.83-2.17-1.45a6.773 6.773 0 01-1.45-2.17A6.59 6.59 0 011.21 8c0-.92.17-1.81.53-2.64.34-.81.83-1.55 1.45-2.17.62-.62 1.36-1.11 2.17-1.45A6.59 6.59 0 018 1.21c.92 0 1.81.17 2.64.53.81.34 1.55.83 2.17 1.45.62.62 1.11 1.36 1.45 2.17.36.83.53 1.72.53 2.64 0 .92-.17 1.81-.53 2.64-.34.81-.83 1.55-1.45 2.17zM4 6.8v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2H5.2C4.53 8 4 7.47 4 6.8zm5 0v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2h-.59C9.53 8 9 7.47 9 6.8zm4 3.2c-.72 1.88-2.91 3-5 3s-4.28-1.13-5-3c-.14-.39.23-1 .66-1h8.59c.41 0 .89.61.75 1z"/></svg>
          </div>
        </div>
        <div class="
          d-inline-block v-align-middle
          
          
           css-truncate css-truncate-target 
           user-status-message-wrapper f6"
           style="line-height: 20px;" >
          <div class="d-inline-block text-gray-dark v-align-text-top text-left">
              <span class="text-gray ml-2">Set status</span>
          </div>
        </div>
      </div>
    </summary>
    <details-dialog class="details-dialog rounded-1 anim-fade-in fast Box Box--overlay" role="dialog" tabindex="-1">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="position-relative flex-auto js-user-status-form" action="/users/status?compact=1&amp;link_mentions=0&amp;truncate=1" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="09lbTDWS8vcqquaXGExKA6wF6KgEoSYxkC8fNiKuzHdVcNi0N3gkXTZStZxhFwF3WjZnStb70qSStrnflpiDnQ==" />
        <div class="Box-header bg-gray border-bottom p-3">
          <button class="Box-btn-octicon js-toggle-user-status-edit btn-octicon float-right" type="reset" aria-label="Close dialog" data-close-dialog>
            <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
          </button>
          <h3 class="Box-title f5 text-bold text-gray-dark">Edit status</h3>
        </div>
        <input type="hidden" name="emoji" class="js-user-status-emoji-field" value="">
        <input type="hidden" name="organization_id" class="js-user-status-org-id-field" value="">
        <div class="px-3 py-2 text-gray-dark">
          <div class="js-characters-remaining-container position-relative mt-2">
            <div class="input-group d-table form-group my-0 js-user-status-form-group">
              <span class="input-group-button d-table-cell v-align-middle" style="width: 1%">
                <button type="button" aria-label="Choose an emoji" class="btn-outline btn js-toggle-user-status-emoji-picker btn-open-emoji-picker p-0">
                  <span class="js-user-status-original-emoji" hidden></span>
                  <span class="js-user-status-custom-emoji"></span>
                  <span class="js-user-status-no-emoji-icon" >
                    <svg class="octicon octicon-smiley" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8s3.58 8 8 8 8-3.58 8-8-3.58-8-8-8zm4.81 12.81a6.72 6.72 0 01-2.17 1.45c-.83.36-1.72.53-2.64.53-.92 0-1.81-.17-2.64-.53-.81-.34-1.55-.83-2.17-1.45a6.773 6.773 0 01-1.45-2.17A6.59 6.59 0 011.21 8c0-.92.17-1.81.53-2.64.34-.81.83-1.55 1.45-2.17.62-.62 1.36-1.11 2.17-1.45A6.59 6.59 0 018 1.21c.92 0 1.81.17 2.64.53.81.34 1.55.83 2.17 1.45.62.62 1.11 1.36 1.45 2.17.36.83.53 1.72.53 2.64 0 .92-.17 1.81-.53 2.64-.34.81-.83 1.55-1.45 2.17zM4 6.8v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2H5.2C4.53 8 4 7.47 4 6.8zm5 0v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2h-.59C9.53 8 9 7.47 9 6.8zm4 3.2c-.72 1.88-2.91 3-5 3s-4.28-1.13-5-3c-.14-.39.23-1 .66-1h8.59c.41 0 .89.61.75 1z"/></svg>
                  </span>
                </button>
              </span>
              <text-expander keys=": @" data-mention-url="/autocomplete/user-suggestions" data-emoji-url="/autocomplete/emoji">
                <input
                  type="text"
                  autocomplete="off"
                  data-no-org-url="/autocomplete/user-suggestions"
                  data-org-url="/suggestions?mention_suggester=1"
                  data-maxlength="80"
                  class="d-table-cell width-full form-control js-user-status-message-field js-characters-remaining-field"
                  placeholder="What's happening?"
                  name="message"
                  value=""
                  aria-label="What is your current status?">
              </text-expander>
              <div class="error">Could not update your status, please try again.</div>
            </div>
            <div style="margin-left: 53px" class="my-1 text-small label-characters-remaining js-characters-remaining" data-suffix="remaining" hidden>
              80 remaining
            </div>
          </div>
          <include-fragment class="js-user-status-emoji-picker" data-url="/users/status/emoji"></include-fragment>
          <div class="overflow-auto ml-n3 mr-n3 px-3 border-bottom" style="max-height: 33vh">
            <div class="user-status-suggestions js-user-status-suggestions collapsed overflow-hidden">
              <h4 class="f6 text-normal my-3">Suggestions:</h4>
              <div class="mx-3 mt-2 clearfix">
                  <div class="float-left col-6">
                      <button type="button" value=":palm_tree:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="palm_tree" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f334.png">🌴</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          On vacation
                        </div>
                      </button>
                      <button type="button" value=":face_with_thermometer:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="face_with_thermometer" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f912.png">🤒</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Out sick
                        </div>
                      </button>
                  </div>
                  <div class="float-left col-6">
                      <button type="button" value=":house:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="house" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3e0.png">🏠</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Working from home
                        </div>
                      </button>
                      <button type="button" value=":dart:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="dart" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3af.png">🎯</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Focusing
                        </div>
                      </button>
                  </div>
              </div>
            </div>
            <div class="user-status-limited-availability-container">
              <div class="form-checkbox my-0">
                <input type="checkbox" name="limited_availability" value="1" class="js-user-status-limited-availability-checkbox" data-default-message="I may be slow to respond." aria-describedby="limited-availability-help-text-truncate-true-compact-true" id="limited-availability-truncate-true-compact-true">
                <label class="d-block f5 text-gray-dark mb-1" for="limited-availability-truncate-true-compact-true">
                  Busy
                </label>
                <p class="note" id="limited-availability-help-text-truncate-true-compact-true">
                  When others mention you, assign you, or request your review,
                  GitHub will let them know that you have limited availability.
                </p>
              </div>
            </div>
          </div>
            

<div class="d-inline-block f5 mr-2 pt-3 pb-2" >
  <div class="d-inline-block mr-1">
    Clear status
  </div>

  <details class="js-user-status-expire-drop-down f6 dropdown details-reset details-overlay d-inline-block mr-2">
    <summary class="f5 btn-link link-gray-dark border px-2 py-1 rounded-1" aria-haspopup="true">
      <div class="js-user-status-expiration-interval-selected d-inline-block v-align-baseline">
        Never
      </div>
      <div class="dropdown-caret"></div>
    </summary>

    <ul class="dropdown-menu dropdown-menu-se pl-0 overflow-auto" style="width: 220px; max-height: 15.5em">
      <li>
        <button type="button" class="btn-link dropdown-item js-user-status-expire-button ws-normal" title="Never">
          <span class="d-inline-block text-bold mb-1">Never</span>
          <div class="f6 lh-condensed">Keep this status until you clear your status or edit your status.</div>
        </button>
      </li>
      <li class="dropdown-divider" role="none"></li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 30 minutes" value="2019-10-23T02:24:15-04:00">
            in 30 minutes
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 1 hour" value="2019-10-23T02:54:15-04:00">
            in 1 hour
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 4 hours" value="2019-10-23T05:54:15-04:00">
            in 4 hours
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="today" value="2019-10-23T23:59:59-04:00">
            today
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="this week" value="2019-10-27T23:59:59-04:00">
            this week
          </button>
        </li>
    </ul>
  </details>
  <input class="js-user-status-expiration-date-input" type="hidden" name="expires_at" value="">
</div>

          <include-fragment class="js-user-status-org-picker" data-url="/users/status/organizations"></include-fragment>
        </div>
        <div class="d-flex flex-items-center flex-justify-between p-3 border-top">
          <button type="submit" disabled class="width-full btn btn-primary mr-2 js-user-status-submit">
            Set status
          </button>
          <button type="button" disabled class="width-full js-clear-user-status-button btn ml-2 ">
            Clear status
          </button>
        </div>
</form>    </details-dialog>
  </details>
</div>

      </div>
      <div role="none" class="dropdown-divider"></div>


    <a role="menuitem" class="dropdown-item" href="/bkang97" data-ga-click="Header, go to profile, text:your profile">Your profile</a>


    <a role="menuitem" class="dropdown-item" href="/bkang97?tab=repositories" data-ga-click="Header, go to repositories, text:your repositories">Your repositories</a>

    <a role="menuitem" class="dropdown-item" href="/bkang97?tab=projects" data-ga-click="Header, go to projects, text:your projects">Your projects</a>

    <a role="menuitem" class="dropdown-item" href="/bkang97?tab=stars" data-ga-click="Header, go to starred repos, text:your stars">Your stars</a>
      <a role="menuitem" class="dropdown-item" href="https://gist.github.com/mine" data-ga-click="Header, your gists, text:your gists">Your gists</a>



    <div role="none" class="dropdown-divider"></div>
      
<div id="feature-enrollment-toggle" class="hide-sm hide-md feature-preview-details position-relative">
  <button
    type="button"
    class="dropdown-item btn-link"
    role="menuitem"
    data-feature-preview-trigger-url="/users/bkang97/feature_previews"
    data-feature-preview-close-details="{&quot;event_type&quot;:&quot;feature_preview.clicks.close_modal&quot;,&quot;payload&quot;:{&quot;client_id&quot;:&quot;251061907.1570248037&quot;,&quot;originating_request_id&quot;:&quot;C15B:6E33:A84D14:1370F0C:5DAFEAFA&quot;,&quot;originating_url&quot;:&quot;https://github.com/keras-team/keras/blob/master/docs/templates/getting-started/sequential-model-guide.md&quot;,&quot;referrer&quot;:&quot;https://github.com/keras-team/keras/tree/master/docs/templates/getting-started&quot;,&quot;user_id&quot;:16846337}}"
    data-feature-preview-close-hmac="b0afa7fb0b67ed41f95d0ac5b69fe474fc8d12d1b4836a2b1e7b7e2b5319753b"
    data-hydro-click="{&quot;event_type&quot;:&quot;feature_preview.clicks.open_modal&quot;,&quot;payload&quot;:{&quot;link_location&quot;:&quot;user_dropdown&quot;,&quot;client_id&quot;:&quot;251061907.1570248037&quot;,&quot;originating_request_id&quot;:&quot;C15B:6E33:A84D14:1370F0C:5DAFEAFA&quot;,&quot;originating_url&quot;:&quot;https://github.com/keras-team/keras/blob/master/docs/templates/getting-started/sequential-model-guide.md&quot;,&quot;referrer&quot;:&quot;https://github.com/keras-team/keras/tree/master/docs/templates/getting-started&quot;,&quot;user_id&quot;:16846337}}"
    data-hydro-click-hmac="f4e884799a6380c4542c2bf48e15b4f482cc9a75ce3cd434037f6ba35507c0d4"
  >
    Feature preview
  </button>
</div>

    <a role="menuitem" class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">Help</a>
    <a role="menuitem" class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">Settings</a>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="logout-form" action="/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="PRkW9mCUWz/5Wrj0M2cjgeGcR5513e1Ic9BZ+fpuDB4eazL9drMQiX84Qcy6HwlmYHdudFFZn+ilBjU+sFHIFA==" />
      
      <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout" role="menuitem">
        Sign out
      </button>
</form>  </details-menu>
</details>

    </div>

  </header>

      

  </div>

  <div id="start-of-content" class="show-on-focus"></div>


    <div id="js-flash-container">

</div>



  <div class="application-main " data-commit-hovercards-enabled>
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main  >
      


  

      <div class="border-bottom shelf intro-shelf js-notice mb-0 pb-4">
  <div class="width-full container">
    <div class="width-full mx-auto shelf-content">
      <h2 class="shelf-title">Learn Git and GitHub without any code!</h2>
      <p class="shelf-lead">
          Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.
      </p>
      <a class="btn btn-primary shelf-cta" target="_blank" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;READ_GUIDE&quot;,&quot;repository_id&quot;:33015583,&quot;client_id&quot;:&quot;251061907.1570248037&quot;,&quot;originating_request_id&quot;:&quot;C15B:6E33:A84D14:1370F0C:5DAFEAFA&quot;,&quot;originating_url&quot;:&quot;https://github.com/keras-team/keras/blob/master/docs/templates/getting-started/sequential-model-guide.md&quot;,&quot;referrer&quot;:&quot;https://github.com/keras-team/keras/tree/master/docs/templates/getting-started&quot;,&quot;user_id&quot;:16846337}}" data-hydro-click-hmac="d93eb406252b70179d78c4c2701e796d77c1a4edcd5c0c9fb5abf819ebc53766" href="https://guides.github.com/activities/hello-world/">Read the guide</a>
    </div>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="shelf-dismiss js-notice-dismiss" action="/dashboard/dismiss_bootcamp" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="delete" /><input type="hidden" name="authenticity_token" value="yx/rOiY+CJxjw9PT2M5BwaV70r6zakXPoenp0DwZkwqpcEgjZGIci1DzPzAnhMSGP7gDJvmIq1Hj2HBGfgi3IQ==" />
      <button name="button" type="submit" class="mr-1 close-button tooltipped tooltipped-w" aria-label="Hide this notice forever" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;DISMISS_BANNER&quot;,&quot;repository_id&quot;:33015583,&quot;client_id&quot;:&quot;251061907.1570248037&quot;,&quot;originating_request_id&quot;:&quot;C15B:6E33:A84D14:1370F0C:5DAFEAFA&quot;,&quot;originating_url&quot;:&quot;https://github.com/keras-team/keras/blob/master/docs/templates/getting-started/sequential-model-guide.md&quot;,&quot;referrer&quot;:&quot;https://github.com/keras-team/keras/tree/master/docs/templates/getting-started&quot;,&quot;user_id&quot;:16846337}}" data-hydro-click-hmac="9b8b964164973d3ad0fb75d874c973480fc1a1bbf5e5c4f0da6d931fd1e75b60">
        <svg aria-label="Hide this notice forever" class="octicon octicon-x v-align-text-top" viewBox="0 0 12 16" version="1.1" width="12" height="16" role="img"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
</button></form>  </div>
</div>



  









  <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav pt-0 pt-lg-4 ">
    <div class="repohead-details-container clearfix container-lg p-responsive d-none d-lg-block">

      <ul class="pagehead-actions">



    <li >
      
    <details class="dropdown details-reset details-overlay d-inline-block float-left"
      data-deferred-details-content-url="/keras-team/keras/used_by_contents"
    >
      <summary class="btn btn-sm btn-with-count" data-menu-button>
        <svg class="octicon octicon-package v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1 4.27v7.47c0 .45.3.84.75.97l6.5 1.73c.16.05.34.05.5 0l6.5-1.73c.45-.13.75-.52.75-.97V4.27c0-.45-.3-.84-.75-.97l-6.5-1.74a1.4 1.4 0 00-.5 0L1.75 3.3c-.45.13-.75.52-.75.97zm7 9.09l-6-1.59V5l6 1.61v6.75zM2 4l2.5-.67L11 5.06l-2.5.67L2 4zm13 7.77l-6 1.59V6.61l2-.55V8.5l2-.53V5.53L15 5v6.77zm-2-7.24L6.5 2.8l2-.53L15 4l-2 .53z"/></svg>
        Used by
        <div class="dropdown-caret"></div>
      </summary>
      <include-fragment>
        <div class="dropdown-menu dropdown-menu-s p-3 text-center" style="width:360px;">
          <img width="32" height="32" alt="Loading..." class="my-0" src="https://github.githubassets.com/images/spinners/octocat-spinner-64.gif" />
          <p class="pt-1 m-0 f5 text-gray-light">
            Loading dependents...
          </p>
        </div>
      </include-fragment>
    </details>
    <a class="social-count"
      href="/keras-team/keras/network/dependents?package_id=UGFja2FnZS01MjI0OTA4Ng%3D%3D"
      aria-label="34774 repositories depend on this package"
    >
      34.8k
    </a>

    </li>

  <li>
    
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form data-remote="true" class="clearfix js-social-form js-social-container" action="/notifications/subscribe" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="W/vFd4cNbLCrtO7ltUIh80WGW5YkQRtY46ZCiNnzIfsTMN69rfn8w1zJQC3mY5aI1baO8AG1F5maQGirbJ4nHg==" />      <input type="hidden" name="repository_id" value="33015583">

      <details class="details-reset details-overlay select-menu float-left">
        <summary class="select-menu-button float-left btn btn-sm btn-with-count" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;WATCH_BUTTON&quot;,&quot;repository_id&quot;:33015583,&quot;client_id&quot;:&quot;251061907.1570248037&quot;,&quot;originating_request_id&quot;:&quot;C15B:6E33:A84D14:1370F0C:5DAFEAFA&quot;,&quot;originating_url&quot;:&quot;https://github.com/keras-team/keras/blob/master/docs/templates/getting-started/sequential-model-guide.md&quot;,&quot;referrer&quot;:&quot;https://github.com/keras-team/keras/tree/master/docs/templates/getting-started&quot;,&quot;user_id&quot;:16846337}}" data-hydro-click-hmac="ab7c267d136d199de6100437a96a1b0c44fdd278565f6f5cf7b74c1127db540a" data-ga-click="Repository, click Watch settings, action:blob#show">          <span data-menu-button>
              <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
              Watch
          </span>
</summary>        <details-menu
          class="select-menu-modal position-absolute mt-5"
          style="z-index: 99;">
          <div class="select-menu-header">
            <span class="select-menu-title">Notifications</span>
          </div>
          <div class="select-menu-list">
            <button type="submit" name="do" value="included" class="select-menu-item width-full" aria-checked="true" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Not watching</span>
                <span class="description">Be notified only when participating or @mentioned.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                  Watch
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="release_only" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Releases only</span>
                <span class="description">Be notified of new releases, and when participating or @mentioned.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                  Unwatch releases
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="subscribed" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Watching</span>
                <span class="description">Be notified of all conversations.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                  Unwatch
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="ignore" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Ignoring</span>
                <span class="description">Never be notified.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-mute v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 2.81v10.38c0 .67-.81 1-1.28.53L3 10H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h2l3.72-3.72C7.19 1.81 8 2.14 8 2.81zm7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06L11.44 8 9.47 9.97l1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06L13.56 8l1.97-1.97z"/></svg>
                  Stop ignoring
                </span>
              </div>
            </button>
          </div>
        </details-menu>
      </details>
        <a class="social-count js-social-count"
          href="/keras-team/keras/watchers"
          aria-label="2079 users are watching this repository">
          2.1k
        </a>
</form>
  </li>

  <li>
      <div class="js-toggler-container js-social-container starring-container ">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="starred js-social-form" action="/keras-team/keras/unstar" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="j7mnZTBNwatmwwsTshrkrvm/nG0D0yoTXtxuwckk/jeFLn9DZtVOk/rtfcD3OmPQ56dBTCq3nMLUuHuOEmm0Ew==" />
      <input type="hidden" name="context" value="repository"></input>
      <button type="submit" class="btn btn-sm btn-with-count js-toggler-target" aria-label="Unstar this repository" title="Unstar keras-team/keras" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;UNSTAR_BUTTON&quot;,&quot;repository_id&quot;:33015583,&quot;client_id&quot;:&quot;251061907.1570248037&quot;,&quot;originating_request_id&quot;:&quot;C15B:6E33:A84D14:1370F0C:5DAFEAFA&quot;,&quot;originating_url&quot;:&quot;https://github.com/keras-team/keras/blob/master/docs/templates/getting-started/sequential-model-guide.md&quot;,&quot;referrer&quot;:&quot;https://github.com/keras-team/keras/tree/master/docs/templates/getting-started&quot;,&quot;user_id&quot;:16846337}}" data-hydro-click-hmac="5a1684fbb0ad1fb2b285ea647a2192d66d2080abe4e7737ebfc9a7169f55a45c" data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">        <svg class="octicon octicon-star v-align-text-bottom" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>
        Unstar
</button>        <a class="social-count js-social-count" href="/keras-team/keras/stargazers"
           aria-label="44890 users starred this repository">
           44.9k
        </a>
</form>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="unstarred js-social-form" action="/keras-team/keras/star" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="g8nPM7WBnd8QkAlPtRj24GjgX+uLCOKpGgkFAdCjtnfGTvVwACEpZMq3MmjY65XZY0pXUwpPFEdpRTkb3cuNcg==" />
      <input type="hidden" name="context" value="repository"></input>
      <button type="submit" class="btn btn-sm btn-with-count js-toggler-target" aria-label="Unstar this repository" title="Star keras-team/keras" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;STAR_BUTTON&quot;,&quot;repository_id&quot;:33015583,&quot;client_id&quot;:&quot;251061907.1570248037&quot;,&quot;originating_request_id&quot;:&quot;C15B:6E33:A84D14:1370F0C:5DAFEAFA&quot;,&quot;originating_url&quot;:&quot;https://github.com/keras-team/keras/blob/master/docs/templates/getting-started/sequential-model-guide.md&quot;,&quot;referrer&quot;:&quot;https://github.com/keras-team/keras/tree/master/docs/templates/getting-started&quot;,&quot;user_id&quot;:16846337}}" data-hydro-click-hmac="88df49ba9a7d30e7d8cb51edda56012581ee97bae464d6a59a3cdd4511b89d96" data-ga-click="Repository, click star button, action:blob#show; text:Star">        <svg class="octicon octicon-star v-align-text-bottom" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>
        Star
</button>        <a class="social-count js-social-count" href="/keras-team/keras/stargazers"
           aria-label="44890 users starred this repository">
          44.9k
        </a>
</form>  </div>

  </li>

  <li>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="btn-with-count" action="/keras-team/keras/fork" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="PPAQsI5NF/c0zzoQkHNGsBafl/zt/E3JklQOpm5GF0st3S8qhENzdbOqiPXwe1wczh4a1u5dszxav4QFFPrLDg==" />
            <button class="btn btn-sm btn-with-count" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;FORK_BUTTON&quot;,&quot;repository_id&quot;:33015583,&quot;client_id&quot;:&quot;251061907.1570248037&quot;,&quot;originating_request_id&quot;:&quot;C15B:6E33:A84D14:1370F0C:5DAFEAFA&quot;,&quot;originating_url&quot;:&quot;https://github.com/keras-team/keras/blob/master/docs/templates/getting-started/sequential-model-guide.md&quot;,&quot;referrer&quot;:&quot;https://github.com/keras-team/keras/tree/master/docs/templates/getting-started&quot;,&quot;user_id&quot;:16846337}}" data-hydro-click-hmac="95f6c4a4801d08c4c6da99020095c00d95c655546a159de5c4016fdf52a9331d" data-ga-click="Repository, show fork modal, action:blob#show; text:Fork" type="submit" title="Fork your own copy of keras-team/keras to your account" aria-label="Fork your own copy of keras-team/keras to your account">              <svg class="octicon octicon-repo-forked v-align-text-bottom" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 00-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 002 1a1.993 1.993 0 00-1 3.72V6.5l3 3v1.78A1.993 1.993 0 005 15a1.993 1.993 0 001-3.72V9.5l3-3V4.72A1.993 1.993 0 008 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
              Fork
</button></form>
    <a href="/keras-team/keras/network/members" class="social-count"
       aria-label="17084 users forked this repository">
      17.1k
    </a>
  </li>
</ul>

      <h1 class="public ">
    <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a class="url fn" rel="author" data-hovercard-type="organization" data-hovercard-url="/orgs/keras-team/hovercard" href="/keras-team">keras-team</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a data-pjax="#js-repo-pjax-container" href="/keras-team/keras">keras</a></strong>
  

</h1>

    </div>
    
<nav class="hx_reponav reponav js-repo-nav js-sidenav-container-pjax container-lg p-responsive d-none d-lg-block"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
    aria-label="Repository"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a class="js-selected-navigation-item selected reponav-item" itemprop="url" data-hotkey="g c" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /keras-team/keras" href="/keras-team/keras">
      <svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" data-hotkey="g i" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /keras-team/keras/issues" href="/keras-team/keras/issues">
        <svg class="octicon octicon-issue-opened" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 011.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="Counter">2,609</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a data-hotkey="g p" itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /keras-team/keras/pulls" href="/keras-team/keras/pulls">
      <svg class="octicon octicon-git-pull-request" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0010 15a1.993 1.993 0 001-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 00-1 3.72v6.56A1.993 1.993 0 002 15a1.993 1.993 0 001-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">20</span>
      <meta itemprop="position" content="3">
</a>  </span>


    <a data-hotkey="g b" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /keras-team/keras/projects" href="/keras-team/keras/projects">
      <svg class="octicon octicon-project" viewBox="0 0 15 16" version="1.1" width="15" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 00-1 1v14a1 1 0 001 1h13a1 1 0 001-1V1a1 1 0 00-1-1z"/></svg>
      Projects
      <span class="Counter" >1</span>
</a>

    <a class="js-selected-navigation-item reponav-item" data-hotkey="g w" data-selected-links="repo_wiki /keras-team/keras/wiki" href="/keras-team/keras/wiki">
      <svg class="octicon octicon-book" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M3 5h4v1H3V5zm0 3h4V7H3v1zm0 2h4V9H3v1zm11-5h-4v1h4V5zm0 2h-4v1h4V7zm0 2h-4v1h4V9zm2-6v9c0 .55-.45 1-1 1H9.5l-1 1-1-1H2c-.55 0-1-.45-1-1V3c0-.55.45-1 1-1h5.5l1 1 1-1H15c.55 0 1 .45 1 1zm-8 .5L7.5 3H2v9h6V3.5zm7-.5H9.5l-.5.5V12h6V3z"/></svg>
      Wiki
</a>
    <a data-skip-pjax="true" class="js-selected-navigation-item reponav-item" data-selected-links="security alerts policy code_scanning /keras-team/keras/security/advisories" href="/keras-team/keras/security/advisories">
      <svg class="octicon octicon-shield" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 2l7-2 7 2v6.02C14 12.69 8.69 16 7 16c-1.69 0-7-3.31-7-7.98V2zm1 .75L7 1l6 1.75v5.268C13 12.104 8.449 15 7 15c-1.449 0-6-2.896-6-6.982V2.75zm1 .75L7 2v12c-1.207 0-5-2.482-5-5.985V3.5z"/></svg>
      Security
</a>
    <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse people /keras-team/keras/pulse" href="/keras-team/keras/pulse">
      <svg class="octicon octicon-graph" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
      Insights
</a>

</nav>

  <div class="reponav-wrapper reponav-small d-lg-none">
  <nav class="reponav js-reponav text-center no-wrap"
       itemscope
       itemtype="http://schema.org/BreadcrumbList">

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a class="js-selected-navigation-item selected reponav-item" itemprop="url" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /keras-team/keras" href="/keras-team/keras">
        <span itemprop="name">Code</span>
        <meta itemprop="position" content="1">
</a>    </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /keras-team/keras/issues" href="/keras-team/keras/issues">
          <span itemprop="name">Issues</span>
          <span class="Counter">2,609</span>
          <meta itemprop="position" content="2">
</a>      </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /keras-team/keras/pulls" href="/keras-team/keras/pulls">
        <span itemprop="name">Pull requests</span>
        <span class="Counter">20</span>
        <meta itemprop="position" content="3">
</a>    </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /keras-team/keras/projects" href="/keras-team/keras/projects">
          <span itemprop="name">Projects</span>
          <span class="Counter">1</span>
          <meta itemprop="position" content="4">
</a>      </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_wiki /keras-team/keras/wiki" href="/keras-team/keras/wiki">
          <span itemprop="name">Wiki</span>
          <meta itemprop="position" content="5">
</a>      </span>

      <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="security alerts policy code_scanning /keras-team/keras/security/advisories" href="/keras-team/keras/security/advisories">
        <span itemprop="name">Security</span>
        <meta itemprop="position" content="6">
</a>
      <a class="js-selected-navigation-item reponav-item" data-selected-links="pulse /keras-team/keras/pulse" href="/keras-team/keras/pulse">
        Pulse
</a>
      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="community /keras-team/keras/community" href="/keras-team/keras/community">
          Community
</a>      </span>

  </nav>
</div>


  </div>
<div class="container-lg clearfix new-discussion-timeline experiment-repo-nav  p-responsive">
  <div class="repository-content ">

    
    


  


    <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/keras-team/keras/blob/ecac367b2372b5f2326fcd3ddd11718323427f4e/docs/templates/getting-started/sequential-model-guide.md">Permalink</a>

    <!-- blob contrib key: blob_contributors:v21:5404492ff6553b0bf202ccf066dd13f0 -->
      

    <div class="d-flex flex-items-start flex-shrink-0 pb-3 flex-column flex-md-row">
      <span class="d-flex flex-justify-between width-full width-md-auto">
        
<details class="details-reset details-overlay select-menu branch-select-menu  hx_rsm" id="branch-select-menu">
  <summary class="btn btn-sm select-menu-button css-truncate"
           data-hotkey="w"
           title="Switch branches or tags">
    <i>Branch:</i>
    <span class="css-truncate-target" data-menu-button>master</span>
  </summary>

  <details-menu class="select-menu-modal hx_rsm-modal position-absolute" style="z-index: 99;" src="/keras-team/keras/ref-list/master/docs/templates/getting-started/sequential-model-guide.md?source_action=show&amp;source_controller=blob" preload>
    <include-fragment class="select-menu-loading-overlay anim-pulse">
      <svg height="32" class="octicon octicon-octoface" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M14.7 5.34c.13-.32.55-1.59-.13-3.31 0 0-1.05-.33-3.44 1.3-1-.28-2.07-.32-3.13-.32s-2.13.04-3.13.32c-2.39-1.64-3.44-1.3-3.44-1.3-.68 1.72-.26 2.99-.13 3.31C.49 6.21 0 7.33 0 8.69 0 13.84 3.33 15 7.98 15S16 13.84 16 8.69c0-1.36-.49-2.48-1.3-3.35zM8 14.02c-3.3 0-5.98-.15-5.98-3.35 0-.76.38-1.48 1.02-2.07 1.07-.98 2.9-.46 4.96-.46 2.07 0 3.88-.52 4.96.46.65.59 1.02 1.3 1.02 2.07 0 3.19-2.68 3.35-5.98 3.35zM5.49 9.01c-.66 0-1.2.8-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.54-1.78-1.2-1.78zm5.02 0c-.66 0-1.2.79-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.53-1.78-1.2-1.78z"/></svg>
    </include-fragment>
  </details-menu>
</details>

        <div class="BtnGroup flex-shrink-0 d-md-none">
          <a href="/keras-team/keras/find/master"
                class="js-pjax-capture-input btn btn-sm BtnGroup-item"
                data-pjax
                data-hotkey="t">
            Find file
          </a>
          <clipboard-copy value="docs/templates/getting-started/sequential-model-guide.md" class="btn btn-sm BtnGroup-item">
            Copy path
          </clipboard-copy>
        </div>
      </span>
      <h2 id="blob-path" class="breadcrumb flex-auto min-width-0 text-normal flex-md-self-center ml-md-2 mr-md-3 my-2 my-md-0">
        <span class="js-repo-root text-bold"><span class="js-path-segment"><a data-pjax="true" href="/keras-team/keras"><span>keras</span></a></span></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/keras-team/keras/tree/master/docs"><span>docs</span></a></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/keras-team/keras/tree/master/docs/templates"><span>templates</span></a></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/keras-team/keras/tree/master/docs/templates/getting-started"><span>getting-started</span></a></span><span class="separator">/</span><strong class="final-path">sequential-model-guide.md</strong>
      </h2>

      <div class="BtnGroup flex-shrink-0 d-none d-md-inline-block">
        <a href="/keras-team/keras/find/master"
              class="js-pjax-capture-input btn btn-sm BtnGroup-item"
              data-pjax
              data-hotkey="t">
          Find file
        </a>
        <clipboard-copy value="docs/templates/getting-started/sequential-model-guide.md" class="btn btn-sm BtnGroup-item">
          Copy path
        </clipboard-copy>
      </div>
    </div>



    
  <div class="Box Box--condensed d-flex flex-column flex-shrink-0">
      <div class="Box-body d-flex flex-justify-between bg-blue-light flex-column flex-md-row flex-items-start flex-md-items-center">
        <span class="pr-md-4 f6">
          <img class="avatar" width="20" height="20" alt="" src="https://camo.githubusercontent.com/c9ea33c23a308c092395a96f7afebb7c127bf96d/68747470733a2f2f322e67726176617461722e636f6d2f6176617461722f34643139643261326564326239316563633464323832386632336162636439303f643d68747470732533412532462532466769746875622e6769746875626173736574732e636f6d253246696d6167657325324667726176617461727325324667726176617461722d757365722d3432302e706e6726723d6726733d313430" data-canonical-src="https://2.gravatar.com/avatar/4d19d2a2ed2b91ecc4d2828f23abcd90?d=https%3A%2F%2Fgithub.githubassets.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png&amp;r=g&amp;s=140" />
          <span class="text-bold link-gray-dark lh-default v-align-middle">Junyoung Kim</span>
            <span class="lh-default v-align-middle">
              <a data-pjax="true" title="Add a link to the metrics document (#13334)

Link to the metrics document(/metrics) was missing in 'Compilation' section. Added one just as other explained arguments." class="link-gray" href="/keras-team/keras/commit/8a8ef43ffcf8d95d2880da073bbcee73e51aad48">Add a link to the metrics document (</a><a class="issue-link js-issue-link" data-error-text="Failed to load issue title" data-id="495013491" data-permission-text="Issue title is private" data-url="https://github.com/keras-team/keras/issues/13334" data-hovercard-type="pull_request" data-hovercard-url="/keras-team/keras/pull/13334/hovercard" href="https://github.com/keras-team/keras/pull/13334">#13334</a><a data-pjax="true" title="Add a link to the metrics document (#13334)

Link to the metrics document(/metrics) was missing in 'Compilation' section. Added one just as other explained arguments." class="link-gray" href="/keras-team/keras/commit/8a8ef43ffcf8d95d2880da073bbcee73e51aad48">)</a>
            </span>
        </span>
        <span class="d-inline-block flex-shrink-0 v-align-bottom f6 mt-2 mt-md-0">
          <a class="pr-2 text-mono link-gray" href="/keras-team/keras/commit/8a8ef43ffcf8d95d2880da073bbcee73e51aad48" data-pjax>8a8ef43</a>
          <relative-time datetime="2019-09-18T20:35:54Z" class="no-wrap">Sep 19, 2019</relative-time>
        </span>
      </div>

    <div class="Box-body d-flex flex-items-center flex-auto f6 border-bottom-0 flex-wrap" >
      <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark float-left mr-2" id="blob_contributors_box">
        <summary class="btn-link">
          <span><strong>17</strong> contributors</span>
        </summary>
        <details-dialog
          class="Box Box--overlay d-flex flex-column anim-fade-in fast"
          aria-label="Users who have contributed to this file"
          src="/keras-team/keras/contributors/8a8ef43ffcf8d95d2880da073bbcee73e51aad48/docs/templates/getting-started/sequential-model-guide.md/list" preload>
          <div class="Box-header">
            <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog>
              <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
            </button>
            <h3 class="Box-title">
              Users who have contributed to this file
            </h3>
          </div>
          <include-fragment class="octocat-spinner my-3" aria-label="Loading..."></include-fragment>
        </details-dialog>
      </details>
        <span class="">
    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=710255" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/keras-team/keras/commits/8a8ef43ffcf8d95d2880da073bbcee73e51aad48/docs/templates/getting-started/sequential-model-guide.md?author=fchollet">
      <img class="avatar mr-1" src="https://avatars2.githubusercontent.com/u/710255?s=40&amp;v=4" width="20" height="20" alt="@fchollet" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=3098704" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/keras-team/keras/commits/8a8ef43ffcf8d95d2880da073bbcee73e51aad48/docs/templates/getting-started/sequential-model-guide.md?author=Piasy">
      <img class="avatar mr-1" src="https://avatars2.githubusercontent.com/u/3098704?s=40&amp;v=4" width="20" height="20" alt="@Piasy" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=5664717" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/keras-team/keras/commits/8a8ef43ffcf8d95d2880da073bbcee73e51aad48/docs/templates/getting-started/sequential-model-guide.md?author=TobyPDE">
      <img class="avatar mr-1" src="https://avatars2.githubusercontent.com/u/5664717?s=40&amp;v=4" width="20" height="20" alt="@TobyPDE" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=1783594" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/keras-team/keras/commits/8a8ef43ffcf8d95d2880da073bbcee73e51aad48/docs/templates/getting-started/sequential-model-guide.md?author=tonybeltramelli">
      <img class="avatar mr-1" src="https://avatars0.githubusercontent.com/u/1783594?s=40&amp;v=4" width="20" height="20" alt="@tonybeltramelli" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=366810" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/keras-team/keras/commits/8a8ef43ffcf8d95d2880da073bbcee73e51aad48/docs/templates/getting-started/sequential-model-guide.md?author=voyageth">
      <img class="avatar mr-1" src="https://avatars3.githubusercontent.com/u/366810?s=40&amp;v=4" width="20" height="20" alt="@voyageth" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=8701515" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/keras-team/keras/commits/8a8ef43ffcf8d95d2880da073bbcee73e51aad48/docs/templates/getting-started/sequential-model-guide.md?author=ramananbalakrishnan">
      <img class="avatar mr-1" src="https://avatars0.githubusercontent.com/u/8701515?s=40&amp;v=4" width="20" height="20" alt="@ramananbalakrishnan" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=10725096" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/keras-team/keras/commits/8a8ef43ffcf8d95d2880da073bbcee73e51aad48/docs/templates/getting-started/sequential-model-guide.md?author=MoyanZitto">
      <img class="avatar mr-1" src="https://avatars0.githubusercontent.com/u/10725096?s=40&amp;v=4" width="20" height="20" alt="@MoyanZitto" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=7121753" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/keras-team/keras/commits/8a8ef43ffcf8d95d2880da073bbcee73e51aad48/docs/templates/getting-started/sequential-model-guide.md?author=nzw0301">
      <img class="avatar mr-1" src="https://avatars3.githubusercontent.com/u/7121753?s=40&amp;v=4" width="20" height="20" alt="@nzw0301" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=590292" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/keras-team/keras/commits/8a8ef43ffcf8d95d2880da073bbcee73e51aad48/docs/templates/getting-started/sequential-model-guide.md?author=kilotaras">
      <img class="avatar mr-1" src="https://avatars3.githubusercontent.com/u/590292?s=40&amp;v=4" width="20" height="20" alt="@kilotaras" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=19240564" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/keras-team/keras/commits/8a8ef43ffcf8d95d2880da073bbcee73e51aad48/docs/templates/getting-started/sequential-model-guide.md?author=johnjacobkenny">
      <img class="avatar mr-1" src="https://avatars3.githubusercontent.com/u/19240564?s=40&amp;v=4" width="20" height="20" alt="@johnjacobkenny" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=3518950" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/keras-team/keras/commits/8a8ef43ffcf8d95d2880da073bbcee73e51aad48/docs/templates/getting-started/sequential-model-guide.md?author=jlopezpena">
      <img class="avatar mr-1" src="https://avatars1.githubusercontent.com/u/3518950?s=40&amp;v=4" width="20" height="20" alt="@jlopezpena" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=11006006" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/keras-team/keras/commits/8a8ef43ffcf8d95d2880da073bbcee73e51aad48/docs/templates/getting-started/sequential-model-guide.md?author=farizrahman4u">
      <img class="avatar mr-1" src="https://avatars1.githubusercontent.com/u/11006006?s=40&amp;v=4" width="20" height="20" alt="@farizrahman4u" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=5952063" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/keras-team/keras/commits/8a8ef43ffcf8d95d2880da073bbcee73e51aad48/docs/templates/getting-started/sequential-model-guide.md?author=cheekujodhpur">
      <img class="avatar mr-1" src="https://avatars3.githubusercontent.com/u/5952063?s=40&amp;v=4" width="20" height="20" alt="@cheekujodhpur" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=19673623" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/keras-team/keras/commits/8a8ef43ffcf8d95d2880da073bbcee73e51aad48/docs/templates/getting-started/sequential-model-guide.md?author=bdwyer2">
      <img class="avatar mr-1" src="https://avatars2.githubusercontent.com/u/19673623?s=40&amp;v=4" width="20" height="20" alt="@bdwyer2" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=602823" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/keras-team/keras/commits/8a8ef43ffcf8d95d2880da073bbcee73e51aad48/docs/templates/getting-started/sequential-model-guide.md?author=abishekk92">
      <img class="avatar mr-1" src="https://avatars2.githubusercontent.com/u/602823?s=40&amp;v=4" width="20" height="20" alt="@abishekk92" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=118582" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/keras-team/keras/commits/8a8ef43ffcf8d95d2880da073bbcee73e51aad48/docs/templates/getting-started/sequential-model-guide.md?author=arokem">
      <img class="avatar mr-1" src="https://avatars0.githubusercontent.com/u/118582?s=40&amp;v=4" width="20" height="20" alt="@arokem" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=13194870" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/keras-team/keras/commits/8a8ef43ffcf8d95d2880da073bbcee73e51aad48/docs/templates/getting-started/sequential-model-guide.md?author=whjxnyzh">
      <img class="avatar mr-1" src="https://avatars3.githubusercontent.com/u/13194870?s=40&amp;v=4" width="20" height="20" alt="@whjxnyzh" /> 
</a>
</span>

    </div>
  </div>





    <div class="Box mt-3 position-relative">
      
<div class="Box-header py-2 d-flex flex-column flex-shrink-0 flex-md-row flex-md-items-center">
  <div class="text-mono f6 flex-auto pr-3 flex-order-2 flex-md-order-1 mt-2 mt-md-0">

      400 lines (301 sloc)
      <span class="file-info-divider"></span>
    13.1 KB
  </div>

  <div class="d-flex py-1 py-md-0 flex-auto flex-order-1 flex-md-order-2 flex-sm-grow-0 flex-justify-between">

    <div class="BtnGroup">
      <a id="raw-url" class="btn btn-sm BtnGroup-item" href="/keras-team/keras/raw/master/docs/templates/getting-started/sequential-model-guide.md">Raw</a>
        <a class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b" href="/keras-team/keras/blame/master/docs/templates/getting-started/sequential-model-guide.md">Blame</a>
      <a rel="nofollow" class="btn btn-sm BtnGroup-item" href="/keras-team/keras/commits/master/docs/templates/getting-started/sequential-model-guide.md">History</a>
    </div>


    <div>
            <a class="btn-octicon tooltipped tooltipped-nw"
               href="https://desktop.github.com"
               aria-label="Open this file in GitHub Desktop"
               data-ga-click="Repository, open with desktop, type:mac">
                <svg class="octicon octicon-device-desktop" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M15 2H1c-.55 0-1 .45-1 1v9c0 .55.45 1 1 1h5.34c-.25.61-.86 1.39-2.34 2h8c-1.48-.61-2.09-1.39-2.34-2H15c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm0 9H1V3h14v8z"/></svg>
            </a>

            <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form js-update-url-with-hash" action="/keras-team/keras/edit/master/docs/templates/getting-started/sequential-model-guide.md" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="iyxHbs490hiwUy6WXJkBsRCL4bPDEeSrGXOJLa0cVI9uo9p83kCrD3vMwrS0PAbKygHTEAVoBZiJBP1hf5kNgg==" />
              <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
                aria-label="Fork this project and edit the file" data-hotkey="e" data-disable-with>
                <svg class="octicon octicon-pencil" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 011.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
              </button>
</form>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form" action="/keras-team/keras/delete/master/docs/templates/getting-started/sequential-model-guide.md" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="XlEZQJmIOFujx/3Pdg0iOg4ewuBdeFIfYqLjN6MQGsTPFCPN1sELtI3QkF7dYTUl3ai+FBFjm4sg54q3sxbTaw==" />
            <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
              aria-label="Fork this project and delete the file" data-disable-with>
              <svg class="octicon octicon-trashcan" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
            </button>
</form>    </div>
  </div>
</div>




      
  <div id="readme" class="Box-body readme blob instapaper_body js-code-block-container">
    <article class="markdown-body entry-content p-3 p-md-6" itemprop="text"><h1><a id="user-content-getting-started-with-the-keras-sequential-model" class="anchor" aria-hidden="true" href="#getting-started-with-the-keras-sequential-model"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Getting started with the Keras Sequential model</h1>
<p>The <code>Sequential</code> model is a linear stack of layers.</p>
<p>You can create a <code>Sequential</code> model by passing a list of layer instances to the constructor:</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">from</span> keras.models <span class="pl-k">import</span> Sequential
<span class="pl-k">from</span> keras.layers <span class="pl-k">import</span> Dense, Activation

model <span class="pl-k">=</span> Sequential([
    Dense(<span class="pl-c1">32</span>, <span class="pl-v">input_shape</span><span class="pl-k">=</span>(<span class="pl-c1">784</span>,)),
    Activation(<span class="pl-s"><span class="pl-pds">'</span>relu<span class="pl-pds">'</span></span>),
    Dense(<span class="pl-c1">10</span>),
    Activation(<span class="pl-s"><span class="pl-pds">'</span>softmax<span class="pl-pds">'</span></span>),
])</pre></div>
<p>You can also simply add layers via the <code>.add()</code> method:</p>
<div class="highlight highlight-source-python"><pre>model <span class="pl-k">=</span> Sequential()
model.add(Dense(<span class="pl-c1">32</span>, <span class="pl-v">input_dim</span><span class="pl-k">=</span><span class="pl-c1">784</span>))
model.add(Activation(<span class="pl-s"><span class="pl-pds">'</span>relu<span class="pl-pds">'</span></span>))</pre></div>
<hr>
<h2><a id="user-content-specifying-the-input-shape" class="anchor" aria-hidden="true" href="#specifying-the-input-shape"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Specifying the input shape</h2>
<p>The model needs to know what input shape it should expect. For this reason, the first layer in a <code>Sequential</code> model (and only the first, because following layers can do automatic shape inference) needs to receive information about its input shape. There are several possible ways to do this:</p>
<ul>
<li>Pass an <code>input_shape</code> argument to the first layer. This is a shape tuple (a tuple of integers or <code>None</code> entries, where <code>None</code> indicates that any positive integer may be expected). In <code>input_shape</code>, the batch dimension is not included.</li>
<li>Some 2D layers, such as <code>Dense</code>, support the specification of their input shape via the argument <code>input_dim</code>, and some 3D temporal layers support the arguments <code>input_dim</code> and <code>input_length</code>.</li>
<li>If you ever need to specify a fixed batch size for your inputs (this is useful for stateful recurrent networks), you can pass a <code>batch_size</code> argument to a layer. If you pass both <code>batch_size=32</code> and <code>input_shape=(6, 8)</code> to a layer, it will then expect every batch of inputs to have the batch shape <code>(32, 6, 8)</code>.</li>
</ul>
<p>As such, the following snippets are strictly equivalent:</p>
<div class="highlight highlight-source-python"><pre>model <span class="pl-k">=</span> Sequential()
model.add(Dense(<span class="pl-c1">32</span>, <span class="pl-v">input_shape</span><span class="pl-k">=</span>(<span class="pl-c1">784</span>,)))</pre></div>
<div class="highlight highlight-source-python"><pre>model <span class="pl-k">=</span> Sequential()
model.add(Dense(<span class="pl-c1">32</span>, <span class="pl-v">input_dim</span><span class="pl-k">=</span><span class="pl-c1">784</span>))</pre></div>
<hr>
<h2><a id="user-content-compilation" class="anchor" aria-hidden="true" href="#compilation"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Compilation</h2>
<p>Before training a model, you need to configure the learning process, which is done via the <code>compile</code> method. It receives three arguments:</p>
<ul>
<li>An optimizer. This could be the string identifier of an existing optimizer (such as <code>rmsprop</code> or <code>adagrad</code>), or an instance of the <code>Optimizer</code> class. See: <a href="/keras-team/keras/blob/master/optimizers">optimizers</a>.</li>
<li>A loss function. This is the objective that the model will try to minimize. It can be the string identifier of an existing loss function (such as <code>categorical_crossentropy</code> or <code>mse</code>), or it can be an objective function. See: <a href="/keras-team/keras/blob/master/losses">losses</a>.</li>
<li>A list of metrics. For any classification problem you will want to set this to <code>metrics=['accuracy']</code>. A metric could be the string identifier of an existing metric or a custom metric function. See: <a href="/keras-team/keras/blob/master/metrics">metrics</a>.</li>
</ul>
<div class="highlight highlight-source-python"><pre><span class="pl-c"><span class="pl-c">#</span> For a multi-class classification problem</span>
model.compile(<span class="pl-v">optimizer</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>rmsprop<span class="pl-pds">'</span></span>,
              <span class="pl-v">loss</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>categorical_crossentropy<span class="pl-pds">'</span></span>,
              <span class="pl-v">metrics</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">'</span>accuracy<span class="pl-pds">'</span></span>])

<span class="pl-c"><span class="pl-c">#</span> For a binary classification problem</span>
model.compile(<span class="pl-v">optimizer</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>rmsprop<span class="pl-pds">'</span></span>,
              <span class="pl-v">loss</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>binary_crossentropy<span class="pl-pds">'</span></span>,
              <span class="pl-v">metrics</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">'</span>accuracy<span class="pl-pds">'</span></span>])

<span class="pl-c"><span class="pl-c">#</span> For a mean squared error regression problem</span>
model.compile(<span class="pl-v">optimizer</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>rmsprop<span class="pl-pds">'</span></span>,
              <span class="pl-v">loss</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>mse<span class="pl-pds">'</span></span>)

<span class="pl-c"><span class="pl-c">#</span> For custom metrics</span>
<span class="pl-k">import</span> keras.backend <span class="pl-k">as</span> K

<span class="pl-k">def</span> <span class="pl-en">mean_pred</span>(<span class="pl-smi">y_true</span>, <span class="pl-smi">y_pred</span>):
    <span class="pl-k">return</span> K.mean(y_pred)

model.compile(<span class="pl-v">optimizer</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>rmsprop<span class="pl-pds">'</span></span>,
              <span class="pl-v">loss</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>binary_crossentropy<span class="pl-pds">'</span></span>,
              <span class="pl-v">metrics</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">'</span>accuracy<span class="pl-pds">'</span></span>, mean_pred])</pre></div>
<hr>
<h2><a id="user-content-training" class="anchor" aria-hidden="true" href="#training"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Training</h2>
<p>Keras models are trained on Numpy arrays of input data and labels. For training a model, you will typically use the <code>fit</code> function. <a href="/keras-team/keras/blob/master/models/sequential">Read its documentation here</a>.</p>
<div class="highlight highlight-source-python"><pre><span class="pl-c"><span class="pl-c">#</span> For a single-input model with 2 classes (binary classification):</span>

model <span class="pl-k">=</span> Sequential()
model.add(Dense(<span class="pl-c1">32</span>, <span class="pl-v">activation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>relu<span class="pl-pds">'</span></span>, <span class="pl-v">input_dim</span><span class="pl-k">=</span><span class="pl-c1">100</span>))
model.add(Dense(<span class="pl-c1">1</span>, <span class="pl-v">activation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>sigmoid<span class="pl-pds">'</span></span>))
model.compile(<span class="pl-v">optimizer</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>rmsprop<span class="pl-pds">'</span></span>,
              <span class="pl-v">loss</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>binary_crossentropy<span class="pl-pds">'</span></span>,
              <span class="pl-v">metrics</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">'</span>accuracy<span class="pl-pds">'</span></span>])

<span class="pl-c"><span class="pl-c">#</span> Generate dummy data</span>
<span class="pl-k">import</span> numpy <span class="pl-k">as</span> np
data <span class="pl-k">=</span> np.random.random((<span class="pl-c1">1000</span>, <span class="pl-c1">100</span>))
labels <span class="pl-k">=</span> np.random.randint(<span class="pl-c1">2</span>, <span class="pl-v">size</span><span class="pl-k">=</span>(<span class="pl-c1">1000</span>, <span class="pl-c1">1</span>))

<span class="pl-c"><span class="pl-c">#</span> Train the model, iterating on the data in batches of 32 samples</span>
model.fit(data, labels, <span class="pl-v">epochs</span><span class="pl-k">=</span><span class="pl-c1">10</span>, <span class="pl-v">batch_size</span><span class="pl-k">=</span><span class="pl-c1">32</span>)</pre></div>
<div class="highlight highlight-source-python"><pre><span class="pl-c"><span class="pl-c">#</span> For a single-input model with 10 classes (categorical classification):</span>

model <span class="pl-k">=</span> Sequential()
model.add(Dense(<span class="pl-c1">32</span>, <span class="pl-v">activation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>relu<span class="pl-pds">'</span></span>, <span class="pl-v">input_dim</span><span class="pl-k">=</span><span class="pl-c1">100</span>))
model.add(Dense(<span class="pl-c1">10</span>, <span class="pl-v">activation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>softmax<span class="pl-pds">'</span></span>))
model.compile(<span class="pl-v">optimizer</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>rmsprop<span class="pl-pds">'</span></span>,
              <span class="pl-v">loss</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>categorical_crossentropy<span class="pl-pds">'</span></span>,
              <span class="pl-v">metrics</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">'</span>accuracy<span class="pl-pds">'</span></span>])

<span class="pl-c"><span class="pl-c">#</span> Generate dummy data</span>
<span class="pl-k">import</span> numpy <span class="pl-k">as</span> np
data <span class="pl-k">=</span> np.random.random((<span class="pl-c1">1000</span>, <span class="pl-c1">100</span>))
labels <span class="pl-k">=</span> np.random.randint(<span class="pl-c1">10</span>, <span class="pl-v">size</span><span class="pl-k">=</span>(<span class="pl-c1">1000</span>, <span class="pl-c1">1</span>))

<span class="pl-c"><span class="pl-c">#</span> Convert labels to categorical one-hot encoding</span>
one_hot_labels <span class="pl-k">=</span> keras.utils.to_categorical(labels, <span class="pl-v">num_classes</span><span class="pl-k">=</span><span class="pl-c1">10</span>)

<span class="pl-c"><span class="pl-c">#</span> Train the model, iterating on the data in batches of 32 samples</span>
model.fit(data, one_hot_labels, <span class="pl-v">epochs</span><span class="pl-k">=</span><span class="pl-c1">10</span>, <span class="pl-v">batch_size</span><span class="pl-k">=</span><span class="pl-c1">32</span>)</pre></div>
<hr>
<h2><a id="user-content-examples" class="anchor" aria-hidden="true" href="#examples"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Examples</h2>
<p>Here are a few examples to get you started!</p>
<p>In the <a href="https://github.com/keras-team/keras/tree/master/examples">examples folder</a>, you will also find example models for real datasets:</p>
<ul>
<li>CIFAR10 small images classification: Convolutional Neural Network (CNN) with realtime data augmentation</li>
<li>IMDB movie review sentiment classification: LSTM over sequences of words</li>
<li>Reuters newswires topic classification: Multilayer Perceptron (MLP)</li>
<li>MNIST handwritten digits classification: MLP &amp; CNN</li>
<li>Character-level text generation with LSTM</li>
</ul>
<p>...and more.</p>
<h3><a id="user-content-multilayer-perceptron-mlp-for-multi-class-softmax-classification" class="anchor" aria-hidden="true" href="#multilayer-perceptron-mlp-for-multi-class-softmax-classification"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Multilayer Perceptron (MLP) for multi-class softmax classification:</h3>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> keras
<span class="pl-k">from</span> keras.models <span class="pl-k">import</span> Sequential
<span class="pl-k">from</span> keras.layers <span class="pl-k">import</span> Dense, Dropout, Activation
<span class="pl-k">from</span> keras.optimizers <span class="pl-k">import</span> <span class="pl-c1">SGD</span>

<span class="pl-c"><span class="pl-c">#</span> Generate dummy data</span>
<span class="pl-k">import</span> numpy <span class="pl-k">as</span> np
x_train <span class="pl-k">=</span> np.random.random((<span class="pl-c1">1000</span>, <span class="pl-c1">20</span>))
y_train <span class="pl-k">=</span> keras.utils.to_categorical(np.random.randint(<span class="pl-c1">10</span>, <span class="pl-v">size</span><span class="pl-k">=</span>(<span class="pl-c1">1000</span>, <span class="pl-c1">1</span>)), <span class="pl-v">num_classes</span><span class="pl-k">=</span><span class="pl-c1">10</span>)
x_test <span class="pl-k">=</span> np.random.random((<span class="pl-c1">100</span>, <span class="pl-c1">20</span>))
y_test <span class="pl-k">=</span> keras.utils.to_categorical(np.random.randint(<span class="pl-c1">10</span>, <span class="pl-v">size</span><span class="pl-k">=</span>(<span class="pl-c1">100</span>, <span class="pl-c1">1</span>)), <span class="pl-v">num_classes</span><span class="pl-k">=</span><span class="pl-c1">10</span>)

model <span class="pl-k">=</span> Sequential()
<span class="pl-c"><span class="pl-c">#</span> Dense(64) is a fully-connected layer with 64 hidden units.</span>
<span class="pl-c"><span class="pl-c">#</span> in the first layer, you must specify the expected input data shape:</span>
<span class="pl-c"><span class="pl-c">#</span> here, 20-dimensional vectors.</span>
model.add(Dense(<span class="pl-c1">64</span>, <span class="pl-v">activation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>relu<span class="pl-pds">'</span></span>, <span class="pl-v">input_dim</span><span class="pl-k">=</span><span class="pl-c1">20</span>))
model.add(Dropout(<span class="pl-c1">0.5</span>))
model.add(Dense(<span class="pl-c1">64</span>, <span class="pl-v">activation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>relu<span class="pl-pds">'</span></span>))
model.add(Dropout(<span class="pl-c1">0.5</span>))
model.add(Dense(<span class="pl-c1">10</span>, <span class="pl-v">activation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>softmax<span class="pl-pds">'</span></span>))

sgd <span class="pl-k">=</span> SGD(<span class="pl-v">lr</span><span class="pl-k">=</span><span class="pl-c1">0.01</span>, <span class="pl-v">decay</span><span class="pl-k">=</span><span class="pl-c1">1e-6</span>, <span class="pl-v">momentum</span><span class="pl-k">=</span><span class="pl-c1">0.9</span>, <span class="pl-v">nesterov</span><span class="pl-k">=</span><span class="pl-c1">True</span>)
model.compile(<span class="pl-v">loss</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>categorical_crossentropy<span class="pl-pds">'</span></span>,
              <span class="pl-v">optimizer</span><span class="pl-k">=</span>sgd,
              <span class="pl-v">metrics</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">'</span>accuracy<span class="pl-pds">'</span></span>])

model.fit(x_train, y_train,
          <span class="pl-v">epochs</span><span class="pl-k">=</span><span class="pl-c1">20</span>,
          <span class="pl-v">batch_size</span><span class="pl-k">=</span><span class="pl-c1">128</span>)
score <span class="pl-k">=</span> model.evaluate(x_test, y_test, <span class="pl-v">batch_size</span><span class="pl-k">=</span><span class="pl-c1">128</span>)</pre></div>
<h3><a id="user-content-mlp-for-binary-classification" class="anchor" aria-hidden="true" href="#mlp-for-binary-classification"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>MLP for binary classification:</h3>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> numpy <span class="pl-k">as</span> np
<span class="pl-k">from</span> keras.models <span class="pl-k">import</span> Sequential
<span class="pl-k">from</span> keras.layers <span class="pl-k">import</span> Dense, Dropout

<span class="pl-c"><span class="pl-c">#</span> Generate dummy data</span>
x_train <span class="pl-k">=</span> np.random.random((<span class="pl-c1">1000</span>, <span class="pl-c1">20</span>))
y_train <span class="pl-k">=</span> np.random.randint(<span class="pl-c1">2</span>, <span class="pl-v">size</span><span class="pl-k">=</span>(<span class="pl-c1">1000</span>, <span class="pl-c1">1</span>))
x_test <span class="pl-k">=</span> np.random.random((<span class="pl-c1">100</span>, <span class="pl-c1">20</span>))
y_test <span class="pl-k">=</span> np.random.randint(<span class="pl-c1">2</span>, <span class="pl-v">size</span><span class="pl-k">=</span>(<span class="pl-c1">100</span>, <span class="pl-c1">1</span>))

model <span class="pl-k">=</span> Sequential()
model.add(Dense(<span class="pl-c1">64</span>, <span class="pl-v">input_dim</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">activation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>relu<span class="pl-pds">'</span></span>))
model.add(Dropout(<span class="pl-c1">0.5</span>))
model.add(Dense(<span class="pl-c1">64</span>, <span class="pl-v">activation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>relu<span class="pl-pds">'</span></span>))
model.add(Dropout(<span class="pl-c1">0.5</span>))
model.add(Dense(<span class="pl-c1">1</span>, <span class="pl-v">activation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>sigmoid<span class="pl-pds">'</span></span>))

model.compile(<span class="pl-v">loss</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>binary_crossentropy<span class="pl-pds">'</span></span>,
              <span class="pl-v">optimizer</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>rmsprop<span class="pl-pds">'</span></span>,
              <span class="pl-v">metrics</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">'</span>accuracy<span class="pl-pds">'</span></span>])

model.fit(x_train, y_train,
          <span class="pl-v">epochs</span><span class="pl-k">=</span><span class="pl-c1">20</span>,
          <span class="pl-v">batch_size</span><span class="pl-k">=</span><span class="pl-c1">128</span>)
score <span class="pl-k">=</span> model.evaluate(x_test, y_test, <span class="pl-v">batch_size</span><span class="pl-k">=</span><span class="pl-c1">128</span>)</pre></div>
<h3><a id="user-content-vgg-like-convnet" class="anchor" aria-hidden="true" href="#vgg-like-convnet"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>VGG-like convnet:</h3>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> numpy <span class="pl-k">as</span> np
<span class="pl-k">import</span> keras
<span class="pl-k">from</span> keras.models <span class="pl-k">import</span> Sequential
<span class="pl-k">from</span> keras.layers <span class="pl-k">import</span> Dense, Dropout, Flatten
<span class="pl-k">from</span> keras.layers <span class="pl-k">import</span> Conv2D, MaxPooling2D
<span class="pl-k">from</span> keras.optimizers <span class="pl-k">import</span> <span class="pl-c1">SGD</span>

<span class="pl-c"><span class="pl-c">#</span> Generate dummy data</span>
x_train <span class="pl-k">=</span> np.random.random((<span class="pl-c1">100</span>, <span class="pl-c1">100</span>, <span class="pl-c1">100</span>, <span class="pl-c1">3</span>))
y_train <span class="pl-k">=</span> keras.utils.to_categorical(np.random.randint(<span class="pl-c1">10</span>, <span class="pl-v">size</span><span class="pl-k">=</span>(<span class="pl-c1">100</span>, <span class="pl-c1">1</span>)), <span class="pl-v">num_classes</span><span class="pl-k">=</span><span class="pl-c1">10</span>)
x_test <span class="pl-k">=</span> np.random.random((<span class="pl-c1">20</span>, <span class="pl-c1">100</span>, <span class="pl-c1">100</span>, <span class="pl-c1">3</span>))
y_test <span class="pl-k">=</span> keras.utils.to_categorical(np.random.randint(<span class="pl-c1">10</span>, <span class="pl-v">size</span><span class="pl-k">=</span>(<span class="pl-c1">20</span>, <span class="pl-c1">1</span>)), <span class="pl-v">num_classes</span><span class="pl-k">=</span><span class="pl-c1">10</span>)

model <span class="pl-k">=</span> Sequential()
<span class="pl-c"><span class="pl-c">#</span> input: 100x100 images with 3 channels -&gt; (100, 100, 3) tensors.</span>
<span class="pl-c"><span class="pl-c">#</span> this applies 32 convolution filters of size 3x3 each.</span>
model.add(Conv2D(<span class="pl-c1">32</span>, (<span class="pl-c1">3</span>, <span class="pl-c1">3</span>), <span class="pl-v">activation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>relu<span class="pl-pds">'</span></span>, <span class="pl-v">input_shape</span><span class="pl-k">=</span>(<span class="pl-c1">100</span>, <span class="pl-c1">100</span>, <span class="pl-c1">3</span>)))
model.add(Conv2D(<span class="pl-c1">32</span>, (<span class="pl-c1">3</span>, <span class="pl-c1">3</span>), <span class="pl-v">activation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>relu<span class="pl-pds">'</span></span>))
model.add(MaxPooling2D(<span class="pl-v">pool_size</span><span class="pl-k">=</span>(<span class="pl-c1">2</span>, <span class="pl-c1">2</span>)))
model.add(Dropout(<span class="pl-c1">0.25</span>))

model.add(Conv2D(<span class="pl-c1">64</span>, (<span class="pl-c1">3</span>, <span class="pl-c1">3</span>), <span class="pl-v">activation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>relu<span class="pl-pds">'</span></span>))
model.add(Conv2D(<span class="pl-c1">64</span>, (<span class="pl-c1">3</span>, <span class="pl-c1">3</span>), <span class="pl-v">activation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>relu<span class="pl-pds">'</span></span>))
model.add(MaxPooling2D(<span class="pl-v">pool_size</span><span class="pl-k">=</span>(<span class="pl-c1">2</span>, <span class="pl-c1">2</span>)))
model.add(Dropout(<span class="pl-c1">0.25</span>))

model.add(Flatten())
model.add(Dense(<span class="pl-c1">256</span>, <span class="pl-v">activation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>relu<span class="pl-pds">'</span></span>))
model.add(Dropout(<span class="pl-c1">0.5</span>))
model.add(Dense(<span class="pl-c1">10</span>, <span class="pl-v">activation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>softmax<span class="pl-pds">'</span></span>))

sgd <span class="pl-k">=</span> SGD(<span class="pl-v">lr</span><span class="pl-k">=</span><span class="pl-c1">0.01</span>, <span class="pl-v">decay</span><span class="pl-k">=</span><span class="pl-c1">1e-6</span>, <span class="pl-v">momentum</span><span class="pl-k">=</span><span class="pl-c1">0.9</span>, <span class="pl-v">nesterov</span><span class="pl-k">=</span><span class="pl-c1">True</span>)
model.compile(<span class="pl-v">loss</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>categorical_crossentropy<span class="pl-pds">'</span></span>, <span class="pl-v">optimizer</span><span class="pl-k">=</span>sgd)

model.fit(x_train, y_train, <span class="pl-v">batch_size</span><span class="pl-k">=</span><span class="pl-c1">32</span>, <span class="pl-v">epochs</span><span class="pl-k">=</span><span class="pl-c1">10</span>)
score <span class="pl-k">=</span> model.evaluate(x_test, y_test, <span class="pl-v">batch_size</span><span class="pl-k">=</span><span class="pl-c1">32</span>)</pre></div>
<h3><a id="user-content-sequence-classification-with-lstm" class="anchor" aria-hidden="true" href="#sequence-classification-with-lstm"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Sequence classification with LSTM:</h3>
<div class="highlight highlight-source-python"><pre><span class="pl-k">from</span> keras.models <span class="pl-k">import</span> Sequential
<span class="pl-k">from</span> keras.layers <span class="pl-k">import</span> Dense, Dropout
<span class="pl-k">from</span> keras.layers <span class="pl-k">import</span> Embedding
<span class="pl-k">from</span> keras.layers <span class="pl-k">import</span> <span class="pl-c1">LSTM</span>

max_features <span class="pl-k">=</span> <span class="pl-c1">1024</span>

model <span class="pl-k">=</span> Sequential()
model.add(Embedding(max_features, <span class="pl-v">output_dim</span><span class="pl-k">=</span><span class="pl-c1">256</span>))
model.add(LSTM(<span class="pl-c1">128</span>))
model.add(Dropout(<span class="pl-c1">0.5</span>))
model.add(Dense(<span class="pl-c1">1</span>, <span class="pl-v">activation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>sigmoid<span class="pl-pds">'</span></span>))

model.compile(<span class="pl-v">loss</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>binary_crossentropy<span class="pl-pds">'</span></span>,
              <span class="pl-v">optimizer</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>rmsprop<span class="pl-pds">'</span></span>,
              <span class="pl-v">metrics</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">'</span>accuracy<span class="pl-pds">'</span></span>])

model.fit(x_train, y_train, <span class="pl-v">batch_size</span><span class="pl-k">=</span><span class="pl-c1">16</span>, <span class="pl-v">epochs</span><span class="pl-k">=</span><span class="pl-c1">10</span>)
score <span class="pl-k">=</span> model.evaluate(x_test, y_test, <span class="pl-v">batch_size</span><span class="pl-k">=</span><span class="pl-c1">16</span>)</pre></div>
<h3><a id="user-content-sequence-classification-with-1d-convolutions" class="anchor" aria-hidden="true" href="#sequence-classification-with-1d-convolutions"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Sequence classification with 1D convolutions:</h3>
<div class="highlight highlight-source-python"><pre><span class="pl-k">from</span> keras.models <span class="pl-k">import</span> Sequential
<span class="pl-k">from</span> keras.layers <span class="pl-k">import</span> Dense, Dropout
<span class="pl-k">from</span> keras.layers <span class="pl-k">import</span> Embedding
<span class="pl-k">from</span> keras.layers <span class="pl-k">import</span> Conv1D, GlobalAveragePooling1D, MaxPooling1D

seq_length <span class="pl-k">=</span> <span class="pl-c1">64</span>

model <span class="pl-k">=</span> Sequential()
model.add(Conv1D(<span class="pl-c1">64</span>, <span class="pl-c1">3</span>, <span class="pl-v">activation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>relu<span class="pl-pds">'</span></span>, <span class="pl-v">input_shape</span><span class="pl-k">=</span>(seq_length, <span class="pl-c1">100</span>)))
model.add(Conv1D(<span class="pl-c1">64</span>, <span class="pl-c1">3</span>, <span class="pl-v">activation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>relu<span class="pl-pds">'</span></span>))
model.add(MaxPooling1D(<span class="pl-c1">3</span>))
model.add(Conv1D(<span class="pl-c1">128</span>, <span class="pl-c1">3</span>, <span class="pl-v">activation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>relu<span class="pl-pds">'</span></span>))
model.add(Conv1D(<span class="pl-c1">128</span>, <span class="pl-c1">3</span>, <span class="pl-v">activation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>relu<span class="pl-pds">'</span></span>))
model.add(GlobalAveragePooling1D())
model.add(Dropout(<span class="pl-c1">0.5</span>))
model.add(Dense(<span class="pl-c1">1</span>, <span class="pl-v">activation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>sigmoid<span class="pl-pds">'</span></span>))

model.compile(<span class="pl-v">loss</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>binary_crossentropy<span class="pl-pds">'</span></span>,
              <span class="pl-v">optimizer</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>rmsprop<span class="pl-pds">'</span></span>,
              <span class="pl-v">metrics</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">'</span>accuracy<span class="pl-pds">'</span></span>])

model.fit(x_train, y_train, <span class="pl-v">batch_size</span><span class="pl-k">=</span><span class="pl-c1">16</span>, <span class="pl-v">epochs</span><span class="pl-k">=</span><span class="pl-c1">10</span>)
score <span class="pl-k">=</span> model.evaluate(x_test, y_test, <span class="pl-v">batch_size</span><span class="pl-k">=</span><span class="pl-c1">16</span>)</pre></div>
<h3><a id="user-content-stacked-lstm-for-sequence-classification" class="anchor" aria-hidden="true" href="#stacked-lstm-for-sequence-classification"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Stacked LSTM for sequence classification</h3>
<p>In this model, we stack 3 LSTM layers on top of each other,
making the model capable of learning higher-level temporal representations.</p>
<p>The first two LSTMs return their full output sequences, but the last one only returns
the last step in its output sequence, thus dropping the temporal dimension
(i.e. converting the input sequence into a single vector).</p>
<p><a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/6b79a01788a45370e063403ffe15ea90b81ab725/68747470733a2f2f6b657261732e696f2f696d672f726567756c61725f737461636b65645f6c73746d2e706e67"><img src="https://camo.githubusercontent.com/6b79a01788a45370e063403ffe15ea90b81ab725/68747470733a2f2f6b657261732e696f2f696d672f726567756c61725f737461636b65645f6c73746d2e706e67" alt="stacked LSTM" data-canonical-src="https://keras.io/img/regular_stacked_lstm.png" style="max-width:100%;"></a></p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">from</span> keras.models <span class="pl-k">import</span> Sequential
<span class="pl-k">from</span> keras.layers <span class="pl-k">import</span> <span class="pl-c1">LSTM</span>, Dense
<span class="pl-k">import</span> numpy <span class="pl-k">as</span> np

data_dim <span class="pl-k">=</span> <span class="pl-c1">16</span>
timesteps <span class="pl-k">=</span> <span class="pl-c1">8</span>
num_classes <span class="pl-k">=</span> <span class="pl-c1">10</span>

<span class="pl-c"><span class="pl-c">#</span> expected input data shape: (batch_size, timesteps, data_dim)</span>
model <span class="pl-k">=</span> Sequential()
model.add(LSTM(<span class="pl-c1">32</span>, <span class="pl-v">return_sequences</span><span class="pl-k">=</span><span class="pl-c1">True</span>,
               <span class="pl-v">input_shape</span><span class="pl-k">=</span>(timesteps, data_dim)))  <span class="pl-c"><span class="pl-c">#</span> returns a sequence of vectors of dimension 32</span>
model.add(LSTM(<span class="pl-c1">32</span>, <span class="pl-v">return_sequences</span><span class="pl-k">=</span><span class="pl-c1">True</span>))  <span class="pl-c"><span class="pl-c">#</span> returns a sequence of vectors of dimension 32</span>
model.add(LSTM(<span class="pl-c1">32</span>))  <span class="pl-c"><span class="pl-c">#</span> return a single vector of dimension 32</span>
model.add(Dense(<span class="pl-c1">10</span>, <span class="pl-v">activation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>softmax<span class="pl-pds">'</span></span>))

model.compile(<span class="pl-v">loss</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>categorical_crossentropy<span class="pl-pds">'</span></span>,
              <span class="pl-v">optimizer</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>rmsprop<span class="pl-pds">'</span></span>,
              <span class="pl-v">metrics</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">'</span>accuracy<span class="pl-pds">'</span></span>])

<span class="pl-c"><span class="pl-c">#</span> Generate dummy training data</span>
x_train <span class="pl-k">=</span> np.random.random((<span class="pl-c1">1000</span>, timesteps, data_dim))
y_train <span class="pl-k">=</span> np.random.random((<span class="pl-c1">1000</span>, num_classes))

<span class="pl-c"><span class="pl-c">#</span> Generate dummy validation data</span>
x_val <span class="pl-k">=</span> np.random.random((<span class="pl-c1">100</span>, timesteps, data_dim))
y_val <span class="pl-k">=</span> np.random.random((<span class="pl-c1">100</span>, num_classes))

model.fit(x_train, y_train,
          <span class="pl-v">batch_size</span><span class="pl-k">=</span><span class="pl-c1">64</span>, <span class="pl-v">epochs</span><span class="pl-k">=</span><span class="pl-c1">5</span>,
          <span class="pl-v">validation_data</span><span class="pl-k">=</span>(x_val, y_val))</pre></div>
<h3><a id="user-content-same-stacked-lstm-model-rendered-stateful" class="anchor" aria-hidden="true" href="#same-stacked-lstm-model-rendered-stateful"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Same stacked LSTM model, rendered "stateful"</h3>
<p>A stateful recurrent model is one for which the internal states (memories) obtained after processing a batch
of samples are reused as initial states for the samples of the next batch. This allows to process longer sequences
while keeping computational complexity manageable.</p>
<p><a href="/keras-team/keras/blob/master/getting-started/faq/#how-can-i-use-stateful-rnns">You can read more about stateful RNNs in the FAQ.</a></p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">from</span> keras.models <span class="pl-k">import</span> Sequential
<span class="pl-k">from</span> keras.layers <span class="pl-k">import</span> <span class="pl-c1">LSTM</span>, Dense
<span class="pl-k">import</span> numpy <span class="pl-k">as</span> np

data_dim <span class="pl-k">=</span> <span class="pl-c1">16</span>
timesteps <span class="pl-k">=</span> <span class="pl-c1">8</span>
num_classes <span class="pl-k">=</span> <span class="pl-c1">10</span>
batch_size <span class="pl-k">=</span> <span class="pl-c1">32</span>

<span class="pl-c"><span class="pl-c">#</span> Expected input batch shape: (batch_size, timesteps, data_dim)</span>
<span class="pl-c"><span class="pl-c">#</span> Note that we have to provide the full batch_input_shape since the network is stateful.</span>
<span class="pl-c"><span class="pl-c">#</span> the sample of index i in batch k is the follow-up for the sample i in batch k-1.</span>
model <span class="pl-k">=</span> Sequential()
model.add(LSTM(<span class="pl-c1">32</span>, <span class="pl-v">return_sequences</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">stateful</span><span class="pl-k">=</span><span class="pl-c1">True</span>,
               <span class="pl-v">batch_input_shape</span><span class="pl-k">=</span>(batch_size, timesteps, data_dim)))
model.add(LSTM(<span class="pl-c1">32</span>, <span class="pl-v">return_sequences</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">stateful</span><span class="pl-k">=</span><span class="pl-c1">True</span>))
model.add(LSTM(<span class="pl-c1">32</span>, <span class="pl-v">stateful</span><span class="pl-k">=</span><span class="pl-c1">True</span>))
model.add(Dense(<span class="pl-c1">10</span>, <span class="pl-v">activation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>softmax<span class="pl-pds">'</span></span>))

model.compile(<span class="pl-v">loss</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>categorical_crossentropy<span class="pl-pds">'</span></span>,
              <span class="pl-v">optimizer</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>rmsprop<span class="pl-pds">'</span></span>,
              <span class="pl-v">metrics</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">'</span>accuracy<span class="pl-pds">'</span></span>])

<span class="pl-c"><span class="pl-c">#</span> Generate dummy training data</span>
x_train <span class="pl-k">=</span> np.random.random((batch_size <span class="pl-k">*</span> <span class="pl-c1">10</span>, timesteps, data_dim))
y_train <span class="pl-k">=</span> np.random.random((batch_size <span class="pl-k">*</span> <span class="pl-c1">10</span>, num_classes))

<span class="pl-c"><span class="pl-c">#</span> Generate dummy validation data</span>
x_val <span class="pl-k">=</span> np.random.random((batch_size <span class="pl-k">*</span> <span class="pl-c1">3</span>, timesteps, data_dim))
y_val <span class="pl-k">=</span> np.random.random((batch_size <span class="pl-k">*</span> <span class="pl-c1">3</span>, num_classes))

model.fit(x_train, y_train,
          <span class="pl-v">batch_size</span><span class="pl-k">=</span>batch_size, <span class="pl-v">epochs</span><span class="pl-k">=</span><span class="pl-c1">5</span>, <span class="pl-v">shuffle</span><span class="pl-k">=</span><span class="pl-c1">False</span>,
          <span class="pl-v">validation_data</span><span class="pl-k">=</span>(x_val, y_val))</pre></div>
</article>
  </div>

    </div>

  

  <details class="details-reset details-overlay details-overlay-dark">
    <summary data-hotkey="l" aria-label="Jump to line"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast linejump" aria-label="Jump to line">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-jump-to-line-form Box-body d-flex" action="" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
        <input class="form-control flex-auto mr-3 linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
        <button type="submit" class="btn" data-close-dialog>Go</button>
</form>    </details-dialog>
  </details>

    <div class="Popover anim-scale-in js-tagsearch-popover"
     hidden
     data-tagsearch-url="/keras-team/keras/find-symbols"
     data-tagsearch-ref="master"
     data-tagsearch-path="docs/templates/getting-started/sequential-model-guide.md"
     data-tagsearch-lang="Markdown"
     data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.click_on_symbol&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;click_on_symbol&quot;,&quot;repository_id&quot;:33015583,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Markdown&quot;,&quot;client_id&quot;:&quot;251061907.1570248037&quot;,&quot;originating_request_id&quot;:&quot;C15B:6E33:A84D14:1370F0C:5DAFEAFA&quot;,&quot;originating_url&quot;:&quot;https://github.com/keras-team/keras/blob/master/docs/templates/getting-started/sequential-model-guide.md&quot;,&quot;referrer&quot;:&quot;https://github.com/keras-team/keras/tree/master/docs/templates/getting-started&quot;,&quot;user_id&quot;:16846337}}"
     data-hydro-click-hmac="a963fda24638dbf3a6d74cd2deb64e508e872d8579d08c8e38395c0ef7e0d915">
  <div class="Popover-message Popover-message--large Popover-message--top-left TagsearchPopover mt-1 mb-4 mx-auto Box box-shadow-large">
    <div class="TagsearchPopover-content js-tagsearch-popover-content overflow-auto" style="will-change:transform;">
    </div>
  </div>
</div>



  </div>
</div>

    </main>
  </div>
  

  </div>

        
<div class="footer container-lg width-full p-responsive" role="contentinfo">
  <div class="position-relative d-flex flex-row-reverse flex-lg-row flex-wrap flex-lg-nowrap flex-justify-center flex-lg-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
      <li class="mr-3 mr-lg-0">&copy; 2019 <span title="0.62394s from unicorn-86bcc5d7fb-mc97m">GitHub</span>, Inc.</li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to security, text:security" href="https://github.com/security">Security</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://githubstatus.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com">Help</a></li>
    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon d-none d-lg-block mx-lg-4" href="https://github.com">
      <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
   <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.com/pricing" data-ga-click="Footer, go to Pricing, text:Pricing">Pricing</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>

    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 000 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 00.01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
    </button>
    You can’t perform that action at this time.
  </div>


    
    <script crossorigin="anonymous" integrity="sha512-dPzQazCbp9rL4Xfjw4yOnSXTb1Pu/gKW3og+XVsYvdmBrDSj3OFisaX3360+KLgQjLuBAvNyDery3N2iGSQCVA==" type="application/javascript" src="https://github.githubassets.com/assets/frameworks-5402e77f.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-0V2CD2adDQCT4JbmFwF1wNw0cK1hVOu7/SI1xIS+8BJ3yhUL8xFSQyz/xlKFkeXebkdsmYQKFtyTDeZhrAPMrw==" type="application/javascript" src="https://github.githubassets.com/assets/github-bootstrap-7c880829.js"></script>
    
    
    
  <div class="js-stale-session-flash flash flash-warn flash-banner" hidden
    >
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 000 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 00.01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <span class="js-stale-session-flash-signed-in" hidden>You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="js-stale-session-flash-signed-out" hidden>You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark hx_rsm" open>
    <summary role="button" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast hx_rsm-dialog hx_rsm-modal">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>

  <div aria-live="polite" class="js-global-screen-reader-notice sr-only"></div>

  </body>
</html>

