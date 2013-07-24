


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>xbmcstubs/xbmcgui.py at master · Tenzer/xbmcstubs · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="https://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <meta property="og:image" content="https://github.global.ssl.fastly.net/images/modules/logos_page/Octocat.png">
    <meta name="hostname" content="fe3.rs.github.com">
    <link rel="assets" href="https://github.global.ssl.fastly.net/">
    <link rel="xhr-socket" href="/_sockets" />
    
    


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" />

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="4PHmF/l1fu0aWEewWwCKToIr6S/kiT2GiRVmc4TSJmM=" name="csrf-token" />

    <link href="https://github.global.ssl.fastly.net/assets/github-cd232974d4d78665813388bd950adadda3d28318.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://github.global.ssl.fastly.net/assets/github2-02d8290450626963b8341bcf949ab6f840ed92b3.css" media="all" rel="stylesheet" type="text/css" />
    


      <script src="https://github.global.ssl.fastly.net/assets/frameworks-e8054ad804a1cf9e9849130fee5a4a5487b663ed.js" type="text/javascript"></script>
      <script src="https://github.global.ssl.fastly.net/assets/github-71528b1c3b8ab920bd42d04e03554416f58f11d1.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="9ca869644778931d4e65ce5fa40d99a0">

        <link data-pjax-transient rel='permalink' href='/Tenzer/xbmcstubs/blob/be31664f64468bf4d03bdcc2a521aa0418591094/xbmcgui.py'>
  <meta property="og:title" content="xbmcstubs"/>
  <meta property="og:type" content="githubog:gitrepository"/>
  <meta property="og:url" content="https://github.com/Tenzer/xbmcstubs"/>
  <meta property="og:image" content="https://github.global.ssl.fastly.net/images/gravatars/gravatar-user-420.png"/>
  <meta property="og:site_name" content="GitHub"/>
  <meta property="og:description" content="xbmcstubs - Stub python classes for script and addon development"/>

  <meta name="description" content="xbmcstubs - Stub python classes for script and addon development" />

  <meta content="68696" name="octolytics-dimension-user_id" /><meta content="Tenzer" name="octolytics-dimension-user_login" /><meta content="1325360" name="octolytics-dimension-repository_id" /><meta content="Tenzer/xbmcstubs" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="1325360" name="octolytics-dimension-repository_network_root_id" /><meta content="Tenzer/xbmcstubs" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/Tenzer/xbmcstubs/commits/master.atom" rel="alternate" title="Recent Commits to xbmcstubs:master" type="application/atom+xml" />

  </head>


  <body class="logged_out page-blob windows vis-public env-production ">

    <div class="wrapper">
      
      
      


      
      <div class="header header-logged-out">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/">
      <span class="mega-octicon octicon-logo-github"></span>
    </a>

    <div class="header-actions">
        <a class="button primary" href="/signup">Sign up</a>
      <a class="button" href="/login?return_to=%2FTenzer%2Fxbmcstubs%2Fblob%2Fmaster%2Fxbmcgui.py">Sign in</a>
    </div>

    <div class="command-bar js-command-bar  in-repository">


      <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
        <li class="features"><a href="/features">Features</a></li>
          <li class="enterprise"><a href="https://enterprise.github.com/">Enterprise</a></li>
          <li class="blog"><a href="/blog">Blog</a></li>
      </ul>
        <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<input type="text" data-hotkey=" s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    
      data-repo="Tenzer/xbmcstubs"
      data-branch="master"
      data-sha="adb3929bb794d85469030ac9de132f3e3db3d43b"
  >

    <input type="hidden" name="nwo" value="Tenzer/xbmcstubs" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="octicon help tooltipped downwards" title="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
    </div>

  </div>
</div>


      


          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">


  <li>
  <a href="/login?return_to=%2FTenzer%2Fxbmcstubs"
  class="minibutton with-count js-toggler-target star-button entice tooltipped upwards "
  title="You must be signed in to use this feature" rel="nofollow">
  <span class="octicon octicon-star"></span>Star
</a>
<a class="social-count js-social-count" href="/Tenzer/xbmcstubs/stargazers">
  5
</a>

  </li>

    <li>
      <a href="/login?return_to=%2FTenzer%2Fxbmcstubs"
        class="minibutton with-count js-toggler-target fork-button entice tooltipped upwards"
        title="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-git-branch"></span>Fork
      </a>
      <a href="/Tenzer/xbmcstubs/network" class="social-count">
        3
      </a>
    </li>
</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo"></span>
          <span class="author">
            <a href="/Tenzer" class="url fn" itemprop="url" rel="author"><span itemprop="title">Tenzer</span></a></span
          ><span class="repohead-name-divider">/</span><strong
          ><a href="/Tenzer/xbmcstubs" class="js-current-repository js-repo-home-link">xbmcstubs</a></strong>

          <span class="page-context-loader">
            <img alt="Octocat-spinner-32" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">

      <div class="repository-with-sidebar repo-container ">

        <div class="repository-sidebar">
            

<div class="repo-nav repo-nav-full js-repository-container-pjax js-octicon-loaders">
  <div class="repo-nav-contents">
    <ul class="repo-menu">
      <li class="tooltipped leftwards" title="Code">
        <a href="/Tenzer/xbmcstubs" aria-label="Code" class="js-selected-navigation-item selected" data-gotokey="c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /Tenzer/xbmcstubs">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped leftwards" title="Issues">
          <a href="/Tenzer/xbmcstubs/issues" aria-label="Issues" class="js-selected-navigation-item js-disable-pjax" data-gotokey="i" data-selected-links="repo_issues /Tenzer/xbmcstubs/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class='counter'>0</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped leftwards" title="Pull Requests"><a href="/Tenzer/xbmcstubs/pulls" aria-label="Pull Requests" class="js-selected-navigation-item js-disable-pjax" data-gotokey="p" data-selected-links="repo_pulls /Tenzer/xbmcstubs/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>0</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


    </ul>
    <div class="repo-menu-separator"></div>
    <ul class="repo-menu">

      <li class="tooltipped leftwards" title="Pulse">
        <a href="/Tenzer/xbmcstubs/pulse" aria-label="Pulse" class="js-selected-navigation-item " data-pjax="true" data-selected-links="pulse /Tenzer/xbmcstubs/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Graphs">
        <a href="/Tenzer/xbmcstubs/graphs" aria-label="Graphs" class="js-selected-navigation-item " data-pjax="true" data-selected-links="repo_graphs repo_contributors /Tenzer/xbmcstubs/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Network">
        <a href="/Tenzer/xbmcstubs/network" aria-label="Network" class="js-selected-navigation-item js-disable-pjax" data-selected-links="repo_network /Tenzer/xbmcstubs/network">
          <span class="octicon octicon-git-branch"></span> <span class="full-word">Network</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

    </ul>

  </div>
</div>

            <div class="only-with-full-nav">
              

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><strong>HTTPS</strong> clone URL</h3>

  <input type="text" class="clone js-url-field"
         value="https://github.com/Tenzer/xbmcstubs.git" readonly="readonly">

  <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/Tenzer/xbmcstubs.git" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><strong>Subversion</strong> checkout URL</h3>

  <input type="text" class="clone js-url-field"
         value="https://github.com/Tenzer/xbmcstubs" readonly="readonly">

  <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/Tenzer/xbmcstubs" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
</div>



<p class="clone-options">You can clone with
    <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>,
    <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>,
  and <a href="https://help.github.com/articles/which-remote-url-should-i-use">other methods.</a>
</p>


  <a href="http://windows.github.com" class="minibutton sidebar-button">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>

                <a href="/Tenzer/xbmcstubs/archive/master.zip"
                   class="minibutton sidebar-button"
                   title="Download this repository as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
            </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:217b71fad8bba726f91d61c7fc219828 -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:217b71fad8bba726f91d61c7fc219828 -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<a href="/Tenzer/xbmcstubs/find/master" data-pjax data-hotkey="t" style="display:none">Show File Finder</a>

<div class="file-navigation">
  


<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target" data-hotkey="w"
    data-master-branch="master"
    data-ref="master">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-remove-close js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Tenzer/xbmcstubs/blob/Dharma/xbmcgui.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="Dharma" data-skip-pjax="true" rel="nofollow" title="Dharma">Dharma</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Tenzer/xbmcstubs/blob/master/xbmcgui.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" data-skip-pjax="true" rel="nofollow" title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Tenzer/xbmcstubs/blob/Dharma.01/xbmcgui.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="Dharma.01" data-skip-pjax="true" rel="nofollow" title="Dharma.01">Dharma.01</a>
            </div> <!-- /.select-menu-item -->
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/Tenzer/xbmcstubs" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">xbmcstubs</span></a></span></span><span class="separator"> / </span><strong class="final-path">xbmcgui.py</strong> <span class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="xbmcgui.py" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


  
  <div class="commit file-history-tease">
    <img class="main-avatar" height="24" src="https://secure.gravatar.com/avatar/3e99ac637d6f97b5f129118aef8b92c7?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
    <span class="author"><a href="/twinther" rel="author">twinther</a></span>
    <time class="js-relative-date" datetime="2011-12-31T02:31:09-08:00" title="2011-12-31 02:31:09">December 31, 2011</time>
    <div class="commit-title">
        <a href="/Tenzer/xbmcstubs/commit/83dade2974801ec0eca96f424275d6889b6c7854" class="message" data-pjax="true" title="added constant values + #noinspection PyUnusedLocal">added constant values + #noinspection PyUnusedLocal</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>2</strong> contributors</a></p>
          <a class="avatar tooltipped downwards" title="Tenzer" href="/Tenzer/xbmcstubs/commits/master/xbmcgui.py?author=Tenzer"><img height="20" src="https://secure.gravatar.com/avatar/6a6fdd7ce2437edf3c0f2889dbcaafc5?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="twinther" href="/Tenzer/xbmcstubs/commits/master/xbmcgui.py?author=twinther"><img height="20" src="https://secure.gravatar.com/avatar/3e99ac637d6f97b5f129118aef8b92c7?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>


    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
        <li class="facebox-user-list-item">
          <img height="24" src="https://secure.gravatar.com/avatar/6a6fdd7ce2437edf3c0f2889dbcaafc5?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/Tenzer">Tenzer</a>
        </li>
        <li class="facebox-user-list-item">
          <img height="24" src="https://secure.gravatar.com/avatar/3e99ac637d6f97b5f129118aef8b92c7?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/twinther">twinther</a>
        </li>
      </ul>
    </div>
  </div>


<div id="files" class="bubble">
  <div class="file">
    <div class="meta">
      <div class="info">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">file</span>
          <span>1350 lines (1047 sloc)</span>
        <span>45.814 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
              <a class="minibutton js-entice" href=""
                 data-entice="You must be signed in to make or propose changes">Edit</a>
          <a href="/Tenzer/xbmcstubs/raw/master/xbmcgui.py" class="button minibutton " id="raw-url">Raw</a>
            <a href="/Tenzer/xbmcstubs/blame/master/xbmcgui.py" class="button minibutton ">Blame</a>
          <a href="/Tenzer/xbmcstubs/commits/master/xbmcgui.py" class="button minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->
            <a class="minibutton danger empty-icon js-entice" href=""
               data-entice="You must be signed in and on a branch to make or propose changes">
            Delete
          </a>
      </div><!-- /.actions -->

    </div>
        <div class="blob-wrapper data type-python js-blob-data">
      <table class="file-code file-diff">
        <tr class="file-code-line">
          <td class="blob-line-nums">
            <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>
<span id="L262" rel="#L262">262</span>
<span id="L263" rel="#L263">263</span>
<span id="L264" rel="#L264">264</span>
<span id="L265" rel="#L265">265</span>
<span id="L266" rel="#L266">266</span>
<span id="L267" rel="#L267">267</span>
<span id="L268" rel="#L268">268</span>
<span id="L269" rel="#L269">269</span>
<span id="L270" rel="#L270">270</span>
<span id="L271" rel="#L271">271</span>
<span id="L272" rel="#L272">272</span>
<span id="L273" rel="#L273">273</span>
<span id="L274" rel="#L274">274</span>
<span id="L275" rel="#L275">275</span>
<span id="L276" rel="#L276">276</span>
<span id="L277" rel="#L277">277</span>
<span id="L278" rel="#L278">278</span>
<span id="L279" rel="#L279">279</span>
<span id="L280" rel="#L280">280</span>
<span id="L281" rel="#L281">281</span>
<span id="L282" rel="#L282">282</span>
<span id="L283" rel="#L283">283</span>
<span id="L284" rel="#L284">284</span>
<span id="L285" rel="#L285">285</span>
<span id="L286" rel="#L286">286</span>
<span id="L287" rel="#L287">287</span>
<span id="L288" rel="#L288">288</span>
<span id="L289" rel="#L289">289</span>
<span id="L290" rel="#L290">290</span>
<span id="L291" rel="#L291">291</span>
<span id="L292" rel="#L292">292</span>
<span id="L293" rel="#L293">293</span>
<span id="L294" rel="#L294">294</span>
<span id="L295" rel="#L295">295</span>
<span id="L296" rel="#L296">296</span>
<span id="L297" rel="#L297">297</span>
<span id="L298" rel="#L298">298</span>
<span id="L299" rel="#L299">299</span>
<span id="L300" rel="#L300">300</span>
<span id="L301" rel="#L301">301</span>
<span id="L302" rel="#L302">302</span>
<span id="L303" rel="#L303">303</span>
<span id="L304" rel="#L304">304</span>
<span id="L305" rel="#L305">305</span>
<span id="L306" rel="#L306">306</span>
<span id="L307" rel="#L307">307</span>
<span id="L308" rel="#L308">308</span>
<span id="L309" rel="#L309">309</span>
<span id="L310" rel="#L310">310</span>
<span id="L311" rel="#L311">311</span>
<span id="L312" rel="#L312">312</span>
<span id="L313" rel="#L313">313</span>
<span id="L314" rel="#L314">314</span>
<span id="L315" rel="#L315">315</span>
<span id="L316" rel="#L316">316</span>
<span id="L317" rel="#L317">317</span>
<span id="L318" rel="#L318">318</span>
<span id="L319" rel="#L319">319</span>
<span id="L320" rel="#L320">320</span>
<span id="L321" rel="#L321">321</span>
<span id="L322" rel="#L322">322</span>
<span id="L323" rel="#L323">323</span>
<span id="L324" rel="#L324">324</span>
<span id="L325" rel="#L325">325</span>
<span id="L326" rel="#L326">326</span>
<span id="L327" rel="#L327">327</span>
<span id="L328" rel="#L328">328</span>
<span id="L329" rel="#L329">329</span>
<span id="L330" rel="#L330">330</span>
<span id="L331" rel="#L331">331</span>
<span id="L332" rel="#L332">332</span>
<span id="L333" rel="#L333">333</span>
<span id="L334" rel="#L334">334</span>
<span id="L335" rel="#L335">335</span>
<span id="L336" rel="#L336">336</span>
<span id="L337" rel="#L337">337</span>
<span id="L338" rel="#L338">338</span>
<span id="L339" rel="#L339">339</span>
<span id="L340" rel="#L340">340</span>
<span id="L341" rel="#L341">341</span>
<span id="L342" rel="#L342">342</span>
<span id="L343" rel="#L343">343</span>
<span id="L344" rel="#L344">344</span>
<span id="L345" rel="#L345">345</span>
<span id="L346" rel="#L346">346</span>
<span id="L347" rel="#L347">347</span>
<span id="L348" rel="#L348">348</span>
<span id="L349" rel="#L349">349</span>
<span id="L350" rel="#L350">350</span>
<span id="L351" rel="#L351">351</span>
<span id="L352" rel="#L352">352</span>
<span id="L353" rel="#L353">353</span>
<span id="L354" rel="#L354">354</span>
<span id="L355" rel="#L355">355</span>
<span id="L356" rel="#L356">356</span>
<span id="L357" rel="#L357">357</span>
<span id="L358" rel="#L358">358</span>
<span id="L359" rel="#L359">359</span>
<span id="L360" rel="#L360">360</span>
<span id="L361" rel="#L361">361</span>
<span id="L362" rel="#L362">362</span>
<span id="L363" rel="#L363">363</span>
<span id="L364" rel="#L364">364</span>
<span id="L365" rel="#L365">365</span>
<span id="L366" rel="#L366">366</span>
<span id="L367" rel="#L367">367</span>
<span id="L368" rel="#L368">368</span>
<span id="L369" rel="#L369">369</span>
<span id="L370" rel="#L370">370</span>
<span id="L371" rel="#L371">371</span>
<span id="L372" rel="#L372">372</span>
<span id="L373" rel="#L373">373</span>
<span id="L374" rel="#L374">374</span>
<span id="L375" rel="#L375">375</span>
<span id="L376" rel="#L376">376</span>
<span id="L377" rel="#L377">377</span>
<span id="L378" rel="#L378">378</span>
<span id="L379" rel="#L379">379</span>
<span id="L380" rel="#L380">380</span>
<span id="L381" rel="#L381">381</span>
<span id="L382" rel="#L382">382</span>
<span id="L383" rel="#L383">383</span>
<span id="L384" rel="#L384">384</span>
<span id="L385" rel="#L385">385</span>
<span id="L386" rel="#L386">386</span>
<span id="L387" rel="#L387">387</span>
<span id="L388" rel="#L388">388</span>
<span id="L389" rel="#L389">389</span>
<span id="L390" rel="#L390">390</span>
<span id="L391" rel="#L391">391</span>
<span id="L392" rel="#L392">392</span>
<span id="L393" rel="#L393">393</span>
<span id="L394" rel="#L394">394</span>
<span id="L395" rel="#L395">395</span>
<span id="L396" rel="#L396">396</span>
<span id="L397" rel="#L397">397</span>
<span id="L398" rel="#L398">398</span>
<span id="L399" rel="#L399">399</span>
<span id="L400" rel="#L400">400</span>
<span id="L401" rel="#L401">401</span>
<span id="L402" rel="#L402">402</span>
<span id="L403" rel="#L403">403</span>
<span id="L404" rel="#L404">404</span>
<span id="L405" rel="#L405">405</span>
<span id="L406" rel="#L406">406</span>
<span id="L407" rel="#L407">407</span>
<span id="L408" rel="#L408">408</span>
<span id="L409" rel="#L409">409</span>
<span id="L410" rel="#L410">410</span>
<span id="L411" rel="#L411">411</span>
<span id="L412" rel="#L412">412</span>
<span id="L413" rel="#L413">413</span>
<span id="L414" rel="#L414">414</span>
<span id="L415" rel="#L415">415</span>
<span id="L416" rel="#L416">416</span>
<span id="L417" rel="#L417">417</span>
<span id="L418" rel="#L418">418</span>
<span id="L419" rel="#L419">419</span>
<span id="L420" rel="#L420">420</span>
<span id="L421" rel="#L421">421</span>
<span id="L422" rel="#L422">422</span>
<span id="L423" rel="#L423">423</span>
<span id="L424" rel="#L424">424</span>
<span id="L425" rel="#L425">425</span>
<span id="L426" rel="#L426">426</span>
<span id="L427" rel="#L427">427</span>
<span id="L428" rel="#L428">428</span>
<span id="L429" rel="#L429">429</span>
<span id="L430" rel="#L430">430</span>
<span id="L431" rel="#L431">431</span>
<span id="L432" rel="#L432">432</span>
<span id="L433" rel="#L433">433</span>
<span id="L434" rel="#L434">434</span>
<span id="L435" rel="#L435">435</span>
<span id="L436" rel="#L436">436</span>
<span id="L437" rel="#L437">437</span>
<span id="L438" rel="#L438">438</span>
<span id="L439" rel="#L439">439</span>
<span id="L440" rel="#L440">440</span>
<span id="L441" rel="#L441">441</span>
<span id="L442" rel="#L442">442</span>
<span id="L443" rel="#L443">443</span>
<span id="L444" rel="#L444">444</span>
<span id="L445" rel="#L445">445</span>
<span id="L446" rel="#L446">446</span>
<span id="L447" rel="#L447">447</span>
<span id="L448" rel="#L448">448</span>
<span id="L449" rel="#L449">449</span>
<span id="L450" rel="#L450">450</span>
<span id="L451" rel="#L451">451</span>
<span id="L452" rel="#L452">452</span>
<span id="L453" rel="#L453">453</span>
<span id="L454" rel="#L454">454</span>
<span id="L455" rel="#L455">455</span>
<span id="L456" rel="#L456">456</span>
<span id="L457" rel="#L457">457</span>
<span id="L458" rel="#L458">458</span>
<span id="L459" rel="#L459">459</span>
<span id="L460" rel="#L460">460</span>
<span id="L461" rel="#L461">461</span>
<span id="L462" rel="#L462">462</span>
<span id="L463" rel="#L463">463</span>
<span id="L464" rel="#L464">464</span>
<span id="L465" rel="#L465">465</span>
<span id="L466" rel="#L466">466</span>
<span id="L467" rel="#L467">467</span>
<span id="L468" rel="#L468">468</span>
<span id="L469" rel="#L469">469</span>
<span id="L470" rel="#L470">470</span>
<span id="L471" rel="#L471">471</span>
<span id="L472" rel="#L472">472</span>
<span id="L473" rel="#L473">473</span>
<span id="L474" rel="#L474">474</span>
<span id="L475" rel="#L475">475</span>
<span id="L476" rel="#L476">476</span>
<span id="L477" rel="#L477">477</span>
<span id="L478" rel="#L478">478</span>
<span id="L479" rel="#L479">479</span>
<span id="L480" rel="#L480">480</span>
<span id="L481" rel="#L481">481</span>
<span id="L482" rel="#L482">482</span>
<span id="L483" rel="#L483">483</span>
<span id="L484" rel="#L484">484</span>
<span id="L485" rel="#L485">485</span>
<span id="L486" rel="#L486">486</span>
<span id="L487" rel="#L487">487</span>
<span id="L488" rel="#L488">488</span>
<span id="L489" rel="#L489">489</span>
<span id="L490" rel="#L490">490</span>
<span id="L491" rel="#L491">491</span>
<span id="L492" rel="#L492">492</span>
<span id="L493" rel="#L493">493</span>
<span id="L494" rel="#L494">494</span>
<span id="L495" rel="#L495">495</span>
<span id="L496" rel="#L496">496</span>
<span id="L497" rel="#L497">497</span>
<span id="L498" rel="#L498">498</span>
<span id="L499" rel="#L499">499</span>
<span id="L500" rel="#L500">500</span>
<span id="L501" rel="#L501">501</span>
<span id="L502" rel="#L502">502</span>
<span id="L503" rel="#L503">503</span>
<span id="L504" rel="#L504">504</span>
<span id="L505" rel="#L505">505</span>
<span id="L506" rel="#L506">506</span>
<span id="L507" rel="#L507">507</span>
<span id="L508" rel="#L508">508</span>
<span id="L509" rel="#L509">509</span>
<span id="L510" rel="#L510">510</span>
<span id="L511" rel="#L511">511</span>
<span id="L512" rel="#L512">512</span>
<span id="L513" rel="#L513">513</span>
<span id="L514" rel="#L514">514</span>
<span id="L515" rel="#L515">515</span>
<span id="L516" rel="#L516">516</span>
<span id="L517" rel="#L517">517</span>
<span id="L518" rel="#L518">518</span>
<span id="L519" rel="#L519">519</span>
<span id="L520" rel="#L520">520</span>
<span id="L521" rel="#L521">521</span>
<span id="L522" rel="#L522">522</span>
<span id="L523" rel="#L523">523</span>
<span id="L524" rel="#L524">524</span>
<span id="L525" rel="#L525">525</span>
<span id="L526" rel="#L526">526</span>
<span id="L527" rel="#L527">527</span>
<span id="L528" rel="#L528">528</span>
<span id="L529" rel="#L529">529</span>
<span id="L530" rel="#L530">530</span>
<span id="L531" rel="#L531">531</span>
<span id="L532" rel="#L532">532</span>
<span id="L533" rel="#L533">533</span>
<span id="L534" rel="#L534">534</span>
<span id="L535" rel="#L535">535</span>
<span id="L536" rel="#L536">536</span>
<span id="L537" rel="#L537">537</span>
<span id="L538" rel="#L538">538</span>
<span id="L539" rel="#L539">539</span>
<span id="L540" rel="#L540">540</span>
<span id="L541" rel="#L541">541</span>
<span id="L542" rel="#L542">542</span>
<span id="L543" rel="#L543">543</span>
<span id="L544" rel="#L544">544</span>
<span id="L545" rel="#L545">545</span>
<span id="L546" rel="#L546">546</span>
<span id="L547" rel="#L547">547</span>
<span id="L548" rel="#L548">548</span>
<span id="L549" rel="#L549">549</span>
<span id="L550" rel="#L550">550</span>
<span id="L551" rel="#L551">551</span>
<span id="L552" rel="#L552">552</span>
<span id="L553" rel="#L553">553</span>
<span id="L554" rel="#L554">554</span>
<span id="L555" rel="#L555">555</span>
<span id="L556" rel="#L556">556</span>
<span id="L557" rel="#L557">557</span>
<span id="L558" rel="#L558">558</span>
<span id="L559" rel="#L559">559</span>
<span id="L560" rel="#L560">560</span>
<span id="L561" rel="#L561">561</span>
<span id="L562" rel="#L562">562</span>
<span id="L563" rel="#L563">563</span>
<span id="L564" rel="#L564">564</span>
<span id="L565" rel="#L565">565</span>
<span id="L566" rel="#L566">566</span>
<span id="L567" rel="#L567">567</span>
<span id="L568" rel="#L568">568</span>
<span id="L569" rel="#L569">569</span>
<span id="L570" rel="#L570">570</span>
<span id="L571" rel="#L571">571</span>
<span id="L572" rel="#L572">572</span>
<span id="L573" rel="#L573">573</span>
<span id="L574" rel="#L574">574</span>
<span id="L575" rel="#L575">575</span>
<span id="L576" rel="#L576">576</span>
<span id="L577" rel="#L577">577</span>
<span id="L578" rel="#L578">578</span>
<span id="L579" rel="#L579">579</span>
<span id="L580" rel="#L580">580</span>
<span id="L581" rel="#L581">581</span>
<span id="L582" rel="#L582">582</span>
<span id="L583" rel="#L583">583</span>
<span id="L584" rel="#L584">584</span>
<span id="L585" rel="#L585">585</span>
<span id="L586" rel="#L586">586</span>
<span id="L587" rel="#L587">587</span>
<span id="L588" rel="#L588">588</span>
<span id="L589" rel="#L589">589</span>
<span id="L590" rel="#L590">590</span>
<span id="L591" rel="#L591">591</span>
<span id="L592" rel="#L592">592</span>
<span id="L593" rel="#L593">593</span>
<span id="L594" rel="#L594">594</span>
<span id="L595" rel="#L595">595</span>
<span id="L596" rel="#L596">596</span>
<span id="L597" rel="#L597">597</span>
<span id="L598" rel="#L598">598</span>
<span id="L599" rel="#L599">599</span>
<span id="L600" rel="#L600">600</span>
<span id="L601" rel="#L601">601</span>
<span id="L602" rel="#L602">602</span>
<span id="L603" rel="#L603">603</span>
<span id="L604" rel="#L604">604</span>
<span id="L605" rel="#L605">605</span>
<span id="L606" rel="#L606">606</span>
<span id="L607" rel="#L607">607</span>
<span id="L608" rel="#L608">608</span>
<span id="L609" rel="#L609">609</span>
<span id="L610" rel="#L610">610</span>
<span id="L611" rel="#L611">611</span>
<span id="L612" rel="#L612">612</span>
<span id="L613" rel="#L613">613</span>
<span id="L614" rel="#L614">614</span>
<span id="L615" rel="#L615">615</span>
<span id="L616" rel="#L616">616</span>
<span id="L617" rel="#L617">617</span>
<span id="L618" rel="#L618">618</span>
<span id="L619" rel="#L619">619</span>
<span id="L620" rel="#L620">620</span>
<span id="L621" rel="#L621">621</span>
<span id="L622" rel="#L622">622</span>
<span id="L623" rel="#L623">623</span>
<span id="L624" rel="#L624">624</span>
<span id="L625" rel="#L625">625</span>
<span id="L626" rel="#L626">626</span>
<span id="L627" rel="#L627">627</span>
<span id="L628" rel="#L628">628</span>
<span id="L629" rel="#L629">629</span>
<span id="L630" rel="#L630">630</span>
<span id="L631" rel="#L631">631</span>
<span id="L632" rel="#L632">632</span>
<span id="L633" rel="#L633">633</span>
<span id="L634" rel="#L634">634</span>
<span id="L635" rel="#L635">635</span>
<span id="L636" rel="#L636">636</span>
<span id="L637" rel="#L637">637</span>
<span id="L638" rel="#L638">638</span>
<span id="L639" rel="#L639">639</span>
<span id="L640" rel="#L640">640</span>
<span id="L641" rel="#L641">641</span>
<span id="L642" rel="#L642">642</span>
<span id="L643" rel="#L643">643</span>
<span id="L644" rel="#L644">644</span>
<span id="L645" rel="#L645">645</span>
<span id="L646" rel="#L646">646</span>
<span id="L647" rel="#L647">647</span>
<span id="L648" rel="#L648">648</span>
<span id="L649" rel="#L649">649</span>
<span id="L650" rel="#L650">650</span>
<span id="L651" rel="#L651">651</span>
<span id="L652" rel="#L652">652</span>
<span id="L653" rel="#L653">653</span>
<span id="L654" rel="#L654">654</span>
<span id="L655" rel="#L655">655</span>
<span id="L656" rel="#L656">656</span>
<span id="L657" rel="#L657">657</span>
<span id="L658" rel="#L658">658</span>
<span id="L659" rel="#L659">659</span>
<span id="L660" rel="#L660">660</span>
<span id="L661" rel="#L661">661</span>
<span id="L662" rel="#L662">662</span>
<span id="L663" rel="#L663">663</span>
<span id="L664" rel="#L664">664</span>
<span id="L665" rel="#L665">665</span>
<span id="L666" rel="#L666">666</span>
<span id="L667" rel="#L667">667</span>
<span id="L668" rel="#L668">668</span>
<span id="L669" rel="#L669">669</span>
<span id="L670" rel="#L670">670</span>
<span id="L671" rel="#L671">671</span>
<span id="L672" rel="#L672">672</span>
<span id="L673" rel="#L673">673</span>
<span id="L674" rel="#L674">674</span>
<span id="L675" rel="#L675">675</span>
<span id="L676" rel="#L676">676</span>
<span id="L677" rel="#L677">677</span>
<span id="L678" rel="#L678">678</span>
<span id="L679" rel="#L679">679</span>
<span id="L680" rel="#L680">680</span>
<span id="L681" rel="#L681">681</span>
<span id="L682" rel="#L682">682</span>
<span id="L683" rel="#L683">683</span>
<span id="L684" rel="#L684">684</span>
<span id="L685" rel="#L685">685</span>
<span id="L686" rel="#L686">686</span>
<span id="L687" rel="#L687">687</span>
<span id="L688" rel="#L688">688</span>
<span id="L689" rel="#L689">689</span>
<span id="L690" rel="#L690">690</span>
<span id="L691" rel="#L691">691</span>
<span id="L692" rel="#L692">692</span>
<span id="L693" rel="#L693">693</span>
<span id="L694" rel="#L694">694</span>
<span id="L695" rel="#L695">695</span>
<span id="L696" rel="#L696">696</span>
<span id="L697" rel="#L697">697</span>
<span id="L698" rel="#L698">698</span>
<span id="L699" rel="#L699">699</span>
<span id="L700" rel="#L700">700</span>
<span id="L701" rel="#L701">701</span>
<span id="L702" rel="#L702">702</span>
<span id="L703" rel="#L703">703</span>
<span id="L704" rel="#L704">704</span>
<span id="L705" rel="#L705">705</span>
<span id="L706" rel="#L706">706</span>
<span id="L707" rel="#L707">707</span>
<span id="L708" rel="#L708">708</span>
<span id="L709" rel="#L709">709</span>
<span id="L710" rel="#L710">710</span>
<span id="L711" rel="#L711">711</span>
<span id="L712" rel="#L712">712</span>
<span id="L713" rel="#L713">713</span>
<span id="L714" rel="#L714">714</span>
<span id="L715" rel="#L715">715</span>
<span id="L716" rel="#L716">716</span>
<span id="L717" rel="#L717">717</span>
<span id="L718" rel="#L718">718</span>
<span id="L719" rel="#L719">719</span>
<span id="L720" rel="#L720">720</span>
<span id="L721" rel="#L721">721</span>
<span id="L722" rel="#L722">722</span>
<span id="L723" rel="#L723">723</span>
<span id="L724" rel="#L724">724</span>
<span id="L725" rel="#L725">725</span>
<span id="L726" rel="#L726">726</span>
<span id="L727" rel="#L727">727</span>
<span id="L728" rel="#L728">728</span>
<span id="L729" rel="#L729">729</span>
<span id="L730" rel="#L730">730</span>
<span id="L731" rel="#L731">731</span>
<span id="L732" rel="#L732">732</span>
<span id="L733" rel="#L733">733</span>
<span id="L734" rel="#L734">734</span>
<span id="L735" rel="#L735">735</span>
<span id="L736" rel="#L736">736</span>
<span id="L737" rel="#L737">737</span>
<span id="L738" rel="#L738">738</span>
<span id="L739" rel="#L739">739</span>
<span id="L740" rel="#L740">740</span>
<span id="L741" rel="#L741">741</span>
<span id="L742" rel="#L742">742</span>
<span id="L743" rel="#L743">743</span>
<span id="L744" rel="#L744">744</span>
<span id="L745" rel="#L745">745</span>
<span id="L746" rel="#L746">746</span>
<span id="L747" rel="#L747">747</span>
<span id="L748" rel="#L748">748</span>
<span id="L749" rel="#L749">749</span>
<span id="L750" rel="#L750">750</span>
<span id="L751" rel="#L751">751</span>
<span id="L752" rel="#L752">752</span>
<span id="L753" rel="#L753">753</span>
<span id="L754" rel="#L754">754</span>
<span id="L755" rel="#L755">755</span>
<span id="L756" rel="#L756">756</span>
<span id="L757" rel="#L757">757</span>
<span id="L758" rel="#L758">758</span>
<span id="L759" rel="#L759">759</span>
<span id="L760" rel="#L760">760</span>
<span id="L761" rel="#L761">761</span>
<span id="L762" rel="#L762">762</span>
<span id="L763" rel="#L763">763</span>
<span id="L764" rel="#L764">764</span>
<span id="L765" rel="#L765">765</span>
<span id="L766" rel="#L766">766</span>
<span id="L767" rel="#L767">767</span>
<span id="L768" rel="#L768">768</span>
<span id="L769" rel="#L769">769</span>
<span id="L770" rel="#L770">770</span>
<span id="L771" rel="#L771">771</span>
<span id="L772" rel="#L772">772</span>
<span id="L773" rel="#L773">773</span>
<span id="L774" rel="#L774">774</span>
<span id="L775" rel="#L775">775</span>
<span id="L776" rel="#L776">776</span>
<span id="L777" rel="#L777">777</span>
<span id="L778" rel="#L778">778</span>
<span id="L779" rel="#L779">779</span>
<span id="L780" rel="#L780">780</span>
<span id="L781" rel="#L781">781</span>
<span id="L782" rel="#L782">782</span>
<span id="L783" rel="#L783">783</span>
<span id="L784" rel="#L784">784</span>
<span id="L785" rel="#L785">785</span>
<span id="L786" rel="#L786">786</span>
<span id="L787" rel="#L787">787</span>
<span id="L788" rel="#L788">788</span>
<span id="L789" rel="#L789">789</span>
<span id="L790" rel="#L790">790</span>
<span id="L791" rel="#L791">791</span>
<span id="L792" rel="#L792">792</span>
<span id="L793" rel="#L793">793</span>
<span id="L794" rel="#L794">794</span>
<span id="L795" rel="#L795">795</span>
<span id="L796" rel="#L796">796</span>
<span id="L797" rel="#L797">797</span>
<span id="L798" rel="#L798">798</span>
<span id="L799" rel="#L799">799</span>
<span id="L800" rel="#L800">800</span>
<span id="L801" rel="#L801">801</span>
<span id="L802" rel="#L802">802</span>
<span id="L803" rel="#L803">803</span>
<span id="L804" rel="#L804">804</span>
<span id="L805" rel="#L805">805</span>
<span id="L806" rel="#L806">806</span>
<span id="L807" rel="#L807">807</span>
<span id="L808" rel="#L808">808</span>
<span id="L809" rel="#L809">809</span>
<span id="L810" rel="#L810">810</span>
<span id="L811" rel="#L811">811</span>
<span id="L812" rel="#L812">812</span>
<span id="L813" rel="#L813">813</span>
<span id="L814" rel="#L814">814</span>
<span id="L815" rel="#L815">815</span>
<span id="L816" rel="#L816">816</span>
<span id="L817" rel="#L817">817</span>
<span id="L818" rel="#L818">818</span>
<span id="L819" rel="#L819">819</span>
<span id="L820" rel="#L820">820</span>
<span id="L821" rel="#L821">821</span>
<span id="L822" rel="#L822">822</span>
<span id="L823" rel="#L823">823</span>
<span id="L824" rel="#L824">824</span>
<span id="L825" rel="#L825">825</span>
<span id="L826" rel="#L826">826</span>
<span id="L827" rel="#L827">827</span>
<span id="L828" rel="#L828">828</span>
<span id="L829" rel="#L829">829</span>
<span id="L830" rel="#L830">830</span>
<span id="L831" rel="#L831">831</span>
<span id="L832" rel="#L832">832</span>
<span id="L833" rel="#L833">833</span>
<span id="L834" rel="#L834">834</span>
<span id="L835" rel="#L835">835</span>
<span id="L836" rel="#L836">836</span>
<span id="L837" rel="#L837">837</span>
<span id="L838" rel="#L838">838</span>
<span id="L839" rel="#L839">839</span>
<span id="L840" rel="#L840">840</span>
<span id="L841" rel="#L841">841</span>
<span id="L842" rel="#L842">842</span>
<span id="L843" rel="#L843">843</span>
<span id="L844" rel="#L844">844</span>
<span id="L845" rel="#L845">845</span>
<span id="L846" rel="#L846">846</span>
<span id="L847" rel="#L847">847</span>
<span id="L848" rel="#L848">848</span>
<span id="L849" rel="#L849">849</span>
<span id="L850" rel="#L850">850</span>
<span id="L851" rel="#L851">851</span>
<span id="L852" rel="#L852">852</span>
<span id="L853" rel="#L853">853</span>
<span id="L854" rel="#L854">854</span>
<span id="L855" rel="#L855">855</span>
<span id="L856" rel="#L856">856</span>
<span id="L857" rel="#L857">857</span>
<span id="L858" rel="#L858">858</span>
<span id="L859" rel="#L859">859</span>
<span id="L860" rel="#L860">860</span>
<span id="L861" rel="#L861">861</span>
<span id="L862" rel="#L862">862</span>
<span id="L863" rel="#L863">863</span>
<span id="L864" rel="#L864">864</span>
<span id="L865" rel="#L865">865</span>
<span id="L866" rel="#L866">866</span>
<span id="L867" rel="#L867">867</span>
<span id="L868" rel="#L868">868</span>
<span id="L869" rel="#L869">869</span>
<span id="L870" rel="#L870">870</span>
<span id="L871" rel="#L871">871</span>
<span id="L872" rel="#L872">872</span>
<span id="L873" rel="#L873">873</span>
<span id="L874" rel="#L874">874</span>
<span id="L875" rel="#L875">875</span>
<span id="L876" rel="#L876">876</span>
<span id="L877" rel="#L877">877</span>
<span id="L878" rel="#L878">878</span>
<span id="L879" rel="#L879">879</span>
<span id="L880" rel="#L880">880</span>
<span id="L881" rel="#L881">881</span>
<span id="L882" rel="#L882">882</span>
<span id="L883" rel="#L883">883</span>
<span id="L884" rel="#L884">884</span>
<span id="L885" rel="#L885">885</span>
<span id="L886" rel="#L886">886</span>
<span id="L887" rel="#L887">887</span>
<span id="L888" rel="#L888">888</span>
<span id="L889" rel="#L889">889</span>
<span id="L890" rel="#L890">890</span>
<span id="L891" rel="#L891">891</span>
<span id="L892" rel="#L892">892</span>
<span id="L893" rel="#L893">893</span>
<span id="L894" rel="#L894">894</span>
<span id="L895" rel="#L895">895</span>
<span id="L896" rel="#L896">896</span>
<span id="L897" rel="#L897">897</span>
<span id="L898" rel="#L898">898</span>
<span id="L899" rel="#L899">899</span>
<span id="L900" rel="#L900">900</span>
<span id="L901" rel="#L901">901</span>
<span id="L902" rel="#L902">902</span>
<span id="L903" rel="#L903">903</span>
<span id="L904" rel="#L904">904</span>
<span id="L905" rel="#L905">905</span>
<span id="L906" rel="#L906">906</span>
<span id="L907" rel="#L907">907</span>
<span id="L908" rel="#L908">908</span>
<span id="L909" rel="#L909">909</span>
<span id="L910" rel="#L910">910</span>
<span id="L911" rel="#L911">911</span>
<span id="L912" rel="#L912">912</span>
<span id="L913" rel="#L913">913</span>
<span id="L914" rel="#L914">914</span>
<span id="L915" rel="#L915">915</span>
<span id="L916" rel="#L916">916</span>
<span id="L917" rel="#L917">917</span>
<span id="L918" rel="#L918">918</span>
<span id="L919" rel="#L919">919</span>
<span id="L920" rel="#L920">920</span>
<span id="L921" rel="#L921">921</span>
<span id="L922" rel="#L922">922</span>
<span id="L923" rel="#L923">923</span>
<span id="L924" rel="#L924">924</span>
<span id="L925" rel="#L925">925</span>
<span id="L926" rel="#L926">926</span>
<span id="L927" rel="#L927">927</span>
<span id="L928" rel="#L928">928</span>
<span id="L929" rel="#L929">929</span>
<span id="L930" rel="#L930">930</span>
<span id="L931" rel="#L931">931</span>
<span id="L932" rel="#L932">932</span>
<span id="L933" rel="#L933">933</span>
<span id="L934" rel="#L934">934</span>
<span id="L935" rel="#L935">935</span>
<span id="L936" rel="#L936">936</span>
<span id="L937" rel="#L937">937</span>
<span id="L938" rel="#L938">938</span>
<span id="L939" rel="#L939">939</span>
<span id="L940" rel="#L940">940</span>
<span id="L941" rel="#L941">941</span>
<span id="L942" rel="#L942">942</span>
<span id="L943" rel="#L943">943</span>
<span id="L944" rel="#L944">944</span>
<span id="L945" rel="#L945">945</span>
<span id="L946" rel="#L946">946</span>
<span id="L947" rel="#L947">947</span>
<span id="L948" rel="#L948">948</span>
<span id="L949" rel="#L949">949</span>
<span id="L950" rel="#L950">950</span>
<span id="L951" rel="#L951">951</span>
<span id="L952" rel="#L952">952</span>
<span id="L953" rel="#L953">953</span>
<span id="L954" rel="#L954">954</span>
<span id="L955" rel="#L955">955</span>
<span id="L956" rel="#L956">956</span>
<span id="L957" rel="#L957">957</span>
<span id="L958" rel="#L958">958</span>
<span id="L959" rel="#L959">959</span>
<span id="L960" rel="#L960">960</span>
<span id="L961" rel="#L961">961</span>
<span id="L962" rel="#L962">962</span>
<span id="L963" rel="#L963">963</span>
<span id="L964" rel="#L964">964</span>
<span id="L965" rel="#L965">965</span>
<span id="L966" rel="#L966">966</span>
<span id="L967" rel="#L967">967</span>
<span id="L968" rel="#L968">968</span>
<span id="L969" rel="#L969">969</span>
<span id="L970" rel="#L970">970</span>
<span id="L971" rel="#L971">971</span>
<span id="L972" rel="#L972">972</span>
<span id="L973" rel="#L973">973</span>
<span id="L974" rel="#L974">974</span>
<span id="L975" rel="#L975">975</span>
<span id="L976" rel="#L976">976</span>
<span id="L977" rel="#L977">977</span>
<span id="L978" rel="#L978">978</span>
<span id="L979" rel="#L979">979</span>
<span id="L980" rel="#L980">980</span>
<span id="L981" rel="#L981">981</span>
<span id="L982" rel="#L982">982</span>
<span id="L983" rel="#L983">983</span>
<span id="L984" rel="#L984">984</span>
<span id="L985" rel="#L985">985</span>
<span id="L986" rel="#L986">986</span>
<span id="L987" rel="#L987">987</span>
<span id="L988" rel="#L988">988</span>
<span id="L989" rel="#L989">989</span>
<span id="L990" rel="#L990">990</span>
<span id="L991" rel="#L991">991</span>
<span id="L992" rel="#L992">992</span>
<span id="L993" rel="#L993">993</span>
<span id="L994" rel="#L994">994</span>
<span id="L995" rel="#L995">995</span>
<span id="L996" rel="#L996">996</span>
<span id="L997" rel="#L997">997</span>
<span id="L998" rel="#L998">998</span>
<span id="L999" rel="#L999">999</span>
<span id="L1000" rel="#L1000">1000</span>
<span id="L1001" rel="#L1001">1001</span>
<span id="L1002" rel="#L1002">1002</span>
<span id="L1003" rel="#L1003">1003</span>
<span id="L1004" rel="#L1004">1004</span>
<span id="L1005" rel="#L1005">1005</span>
<span id="L1006" rel="#L1006">1006</span>
<span id="L1007" rel="#L1007">1007</span>
<span id="L1008" rel="#L1008">1008</span>
<span id="L1009" rel="#L1009">1009</span>
<span id="L1010" rel="#L1010">1010</span>
<span id="L1011" rel="#L1011">1011</span>
<span id="L1012" rel="#L1012">1012</span>
<span id="L1013" rel="#L1013">1013</span>
<span id="L1014" rel="#L1014">1014</span>
<span id="L1015" rel="#L1015">1015</span>
<span id="L1016" rel="#L1016">1016</span>
<span id="L1017" rel="#L1017">1017</span>
<span id="L1018" rel="#L1018">1018</span>
<span id="L1019" rel="#L1019">1019</span>
<span id="L1020" rel="#L1020">1020</span>
<span id="L1021" rel="#L1021">1021</span>
<span id="L1022" rel="#L1022">1022</span>
<span id="L1023" rel="#L1023">1023</span>
<span id="L1024" rel="#L1024">1024</span>
<span id="L1025" rel="#L1025">1025</span>
<span id="L1026" rel="#L1026">1026</span>
<span id="L1027" rel="#L1027">1027</span>
<span id="L1028" rel="#L1028">1028</span>
<span id="L1029" rel="#L1029">1029</span>
<span id="L1030" rel="#L1030">1030</span>
<span id="L1031" rel="#L1031">1031</span>
<span id="L1032" rel="#L1032">1032</span>
<span id="L1033" rel="#L1033">1033</span>
<span id="L1034" rel="#L1034">1034</span>
<span id="L1035" rel="#L1035">1035</span>
<span id="L1036" rel="#L1036">1036</span>
<span id="L1037" rel="#L1037">1037</span>
<span id="L1038" rel="#L1038">1038</span>
<span id="L1039" rel="#L1039">1039</span>
<span id="L1040" rel="#L1040">1040</span>
<span id="L1041" rel="#L1041">1041</span>
<span id="L1042" rel="#L1042">1042</span>
<span id="L1043" rel="#L1043">1043</span>
<span id="L1044" rel="#L1044">1044</span>
<span id="L1045" rel="#L1045">1045</span>
<span id="L1046" rel="#L1046">1046</span>
<span id="L1047" rel="#L1047">1047</span>
<span id="L1048" rel="#L1048">1048</span>
<span id="L1049" rel="#L1049">1049</span>
<span id="L1050" rel="#L1050">1050</span>
<span id="L1051" rel="#L1051">1051</span>
<span id="L1052" rel="#L1052">1052</span>
<span id="L1053" rel="#L1053">1053</span>
<span id="L1054" rel="#L1054">1054</span>
<span id="L1055" rel="#L1055">1055</span>
<span id="L1056" rel="#L1056">1056</span>
<span id="L1057" rel="#L1057">1057</span>
<span id="L1058" rel="#L1058">1058</span>
<span id="L1059" rel="#L1059">1059</span>
<span id="L1060" rel="#L1060">1060</span>
<span id="L1061" rel="#L1061">1061</span>
<span id="L1062" rel="#L1062">1062</span>
<span id="L1063" rel="#L1063">1063</span>
<span id="L1064" rel="#L1064">1064</span>
<span id="L1065" rel="#L1065">1065</span>
<span id="L1066" rel="#L1066">1066</span>
<span id="L1067" rel="#L1067">1067</span>
<span id="L1068" rel="#L1068">1068</span>
<span id="L1069" rel="#L1069">1069</span>
<span id="L1070" rel="#L1070">1070</span>
<span id="L1071" rel="#L1071">1071</span>
<span id="L1072" rel="#L1072">1072</span>
<span id="L1073" rel="#L1073">1073</span>
<span id="L1074" rel="#L1074">1074</span>
<span id="L1075" rel="#L1075">1075</span>
<span id="L1076" rel="#L1076">1076</span>
<span id="L1077" rel="#L1077">1077</span>
<span id="L1078" rel="#L1078">1078</span>
<span id="L1079" rel="#L1079">1079</span>
<span id="L1080" rel="#L1080">1080</span>
<span id="L1081" rel="#L1081">1081</span>
<span id="L1082" rel="#L1082">1082</span>
<span id="L1083" rel="#L1083">1083</span>
<span id="L1084" rel="#L1084">1084</span>
<span id="L1085" rel="#L1085">1085</span>
<span id="L1086" rel="#L1086">1086</span>
<span id="L1087" rel="#L1087">1087</span>
<span id="L1088" rel="#L1088">1088</span>
<span id="L1089" rel="#L1089">1089</span>
<span id="L1090" rel="#L1090">1090</span>
<span id="L1091" rel="#L1091">1091</span>
<span id="L1092" rel="#L1092">1092</span>
<span id="L1093" rel="#L1093">1093</span>
<span id="L1094" rel="#L1094">1094</span>
<span id="L1095" rel="#L1095">1095</span>
<span id="L1096" rel="#L1096">1096</span>
<span id="L1097" rel="#L1097">1097</span>
<span id="L1098" rel="#L1098">1098</span>
<span id="L1099" rel="#L1099">1099</span>
<span id="L1100" rel="#L1100">1100</span>
<span id="L1101" rel="#L1101">1101</span>
<span id="L1102" rel="#L1102">1102</span>
<span id="L1103" rel="#L1103">1103</span>
<span id="L1104" rel="#L1104">1104</span>
<span id="L1105" rel="#L1105">1105</span>
<span id="L1106" rel="#L1106">1106</span>
<span id="L1107" rel="#L1107">1107</span>
<span id="L1108" rel="#L1108">1108</span>
<span id="L1109" rel="#L1109">1109</span>
<span id="L1110" rel="#L1110">1110</span>
<span id="L1111" rel="#L1111">1111</span>
<span id="L1112" rel="#L1112">1112</span>
<span id="L1113" rel="#L1113">1113</span>
<span id="L1114" rel="#L1114">1114</span>
<span id="L1115" rel="#L1115">1115</span>
<span id="L1116" rel="#L1116">1116</span>
<span id="L1117" rel="#L1117">1117</span>
<span id="L1118" rel="#L1118">1118</span>
<span id="L1119" rel="#L1119">1119</span>
<span id="L1120" rel="#L1120">1120</span>
<span id="L1121" rel="#L1121">1121</span>
<span id="L1122" rel="#L1122">1122</span>
<span id="L1123" rel="#L1123">1123</span>
<span id="L1124" rel="#L1124">1124</span>
<span id="L1125" rel="#L1125">1125</span>
<span id="L1126" rel="#L1126">1126</span>
<span id="L1127" rel="#L1127">1127</span>
<span id="L1128" rel="#L1128">1128</span>
<span id="L1129" rel="#L1129">1129</span>
<span id="L1130" rel="#L1130">1130</span>
<span id="L1131" rel="#L1131">1131</span>
<span id="L1132" rel="#L1132">1132</span>
<span id="L1133" rel="#L1133">1133</span>
<span id="L1134" rel="#L1134">1134</span>
<span id="L1135" rel="#L1135">1135</span>
<span id="L1136" rel="#L1136">1136</span>
<span id="L1137" rel="#L1137">1137</span>
<span id="L1138" rel="#L1138">1138</span>
<span id="L1139" rel="#L1139">1139</span>
<span id="L1140" rel="#L1140">1140</span>
<span id="L1141" rel="#L1141">1141</span>
<span id="L1142" rel="#L1142">1142</span>
<span id="L1143" rel="#L1143">1143</span>
<span id="L1144" rel="#L1144">1144</span>
<span id="L1145" rel="#L1145">1145</span>
<span id="L1146" rel="#L1146">1146</span>
<span id="L1147" rel="#L1147">1147</span>
<span id="L1148" rel="#L1148">1148</span>
<span id="L1149" rel="#L1149">1149</span>
<span id="L1150" rel="#L1150">1150</span>
<span id="L1151" rel="#L1151">1151</span>
<span id="L1152" rel="#L1152">1152</span>
<span id="L1153" rel="#L1153">1153</span>
<span id="L1154" rel="#L1154">1154</span>
<span id="L1155" rel="#L1155">1155</span>
<span id="L1156" rel="#L1156">1156</span>
<span id="L1157" rel="#L1157">1157</span>
<span id="L1158" rel="#L1158">1158</span>
<span id="L1159" rel="#L1159">1159</span>
<span id="L1160" rel="#L1160">1160</span>
<span id="L1161" rel="#L1161">1161</span>
<span id="L1162" rel="#L1162">1162</span>
<span id="L1163" rel="#L1163">1163</span>
<span id="L1164" rel="#L1164">1164</span>
<span id="L1165" rel="#L1165">1165</span>
<span id="L1166" rel="#L1166">1166</span>
<span id="L1167" rel="#L1167">1167</span>
<span id="L1168" rel="#L1168">1168</span>
<span id="L1169" rel="#L1169">1169</span>
<span id="L1170" rel="#L1170">1170</span>
<span id="L1171" rel="#L1171">1171</span>
<span id="L1172" rel="#L1172">1172</span>
<span id="L1173" rel="#L1173">1173</span>
<span id="L1174" rel="#L1174">1174</span>
<span id="L1175" rel="#L1175">1175</span>
<span id="L1176" rel="#L1176">1176</span>
<span id="L1177" rel="#L1177">1177</span>
<span id="L1178" rel="#L1178">1178</span>
<span id="L1179" rel="#L1179">1179</span>
<span id="L1180" rel="#L1180">1180</span>
<span id="L1181" rel="#L1181">1181</span>
<span id="L1182" rel="#L1182">1182</span>
<span id="L1183" rel="#L1183">1183</span>
<span id="L1184" rel="#L1184">1184</span>
<span id="L1185" rel="#L1185">1185</span>
<span id="L1186" rel="#L1186">1186</span>
<span id="L1187" rel="#L1187">1187</span>
<span id="L1188" rel="#L1188">1188</span>
<span id="L1189" rel="#L1189">1189</span>
<span id="L1190" rel="#L1190">1190</span>
<span id="L1191" rel="#L1191">1191</span>
<span id="L1192" rel="#L1192">1192</span>
<span id="L1193" rel="#L1193">1193</span>
<span id="L1194" rel="#L1194">1194</span>
<span id="L1195" rel="#L1195">1195</span>
<span id="L1196" rel="#L1196">1196</span>
<span id="L1197" rel="#L1197">1197</span>
<span id="L1198" rel="#L1198">1198</span>
<span id="L1199" rel="#L1199">1199</span>
<span id="L1200" rel="#L1200">1200</span>
<span id="L1201" rel="#L1201">1201</span>
<span id="L1202" rel="#L1202">1202</span>
<span id="L1203" rel="#L1203">1203</span>
<span id="L1204" rel="#L1204">1204</span>
<span id="L1205" rel="#L1205">1205</span>
<span id="L1206" rel="#L1206">1206</span>
<span id="L1207" rel="#L1207">1207</span>
<span id="L1208" rel="#L1208">1208</span>
<span id="L1209" rel="#L1209">1209</span>
<span id="L1210" rel="#L1210">1210</span>
<span id="L1211" rel="#L1211">1211</span>
<span id="L1212" rel="#L1212">1212</span>
<span id="L1213" rel="#L1213">1213</span>
<span id="L1214" rel="#L1214">1214</span>
<span id="L1215" rel="#L1215">1215</span>
<span id="L1216" rel="#L1216">1216</span>
<span id="L1217" rel="#L1217">1217</span>
<span id="L1218" rel="#L1218">1218</span>
<span id="L1219" rel="#L1219">1219</span>
<span id="L1220" rel="#L1220">1220</span>
<span id="L1221" rel="#L1221">1221</span>
<span id="L1222" rel="#L1222">1222</span>
<span id="L1223" rel="#L1223">1223</span>
<span id="L1224" rel="#L1224">1224</span>
<span id="L1225" rel="#L1225">1225</span>
<span id="L1226" rel="#L1226">1226</span>
<span id="L1227" rel="#L1227">1227</span>
<span id="L1228" rel="#L1228">1228</span>
<span id="L1229" rel="#L1229">1229</span>
<span id="L1230" rel="#L1230">1230</span>
<span id="L1231" rel="#L1231">1231</span>
<span id="L1232" rel="#L1232">1232</span>
<span id="L1233" rel="#L1233">1233</span>
<span id="L1234" rel="#L1234">1234</span>
<span id="L1235" rel="#L1235">1235</span>
<span id="L1236" rel="#L1236">1236</span>
<span id="L1237" rel="#L1237">1237</span>
<span id="L1238" rel="#L1238">1238</span>
<span id="L1239" rel="#L1239">1239</span>
<span id="L1240" rel="#L1240">1240</span>
<span id="L1241" rel="#L1241">1241</span>
<span id="L1242" rel="#L1242">1242</span>
<span id="L1243" rel="#L1243">1243</span>
<span id="L1244" rel="#L1244">1244</span>
<span id="L1245" rel="#L1245">1245</span>
<span id="L1246" rel="#L1246">1246</span>
<span id="L1247" rel="#L1247">1247</span>
<span id="L1248" rel="#L1248">1248</span>
<span id="L1249" rel="#L1249">1249</span>
<span id="L1250" rel="#L1250">1250</span>
<span id="L1251" rel="#L1251">1251</span>
<span id="L1252" rel="#L1252">1252</span>
<span id="L1253" rel="#L1253">1253</span>
<span id="L1254" rel="#L1254">1254</span>
<span id="L1255" rel="#L1255">1255</span>
<span id="L1256" rel="#L1256">1256</span>
<span id="L1257" rel="#L1257">1257</span>
<span id="L1258" rel="#L1258">1258</span>
<span id="L1259" rel="#L1259">1259</span>
<span id="L1260" rel="#L1260">1260</span>
<span id="L1261" rel="#L1261">1261</span>
<span id="L1262" rel="#L1262">1262</span>
<span id="L1263" rel="#L1263">1263</span>
<span id="L1264" rel="#L1264">1264</span>
<span id="L1265" rel="#L1265">1265</span>
<span id="L1266" rel="#L1266">1266</span>
<span id="L1267" rel="#L1267">1267</span>
<span id="L1268" rel="#L1268">1268</span>
<span id="L1269" rel="#L1269">1269</span>
<span id="L1270" rel="#L1270">1270</span>
<span id="L1271" rel="#L1271">1271</span>
<span id="L1272" rel="#L1272">1272</span>
<span id="L1273" rel="#L1273">1273</span>
<span id="L1274" rel="#L1274">1274</span>
<span id="L1275" rel="#L1275">1275</span>
<span id="L1276" rel="#L1276">1276</span>
<span id="L1277" rel="#L1277">1277</span>
<span id="L1278" rel="#L1278">1278</span>
<span id="L1279" rel="#L1279">1279</span>
<span id="L1280" rel="#L1280">1280</span>
<span id="L1281" rel="#L1281">1281</span>
<span id="L1282" rel="#L1282">1282</span>
<span id="L1283" rel="#L1283">1283</span>
<span id="L1284" rel="#L1284">1284</span>
<span id="L1285" rel="#L1285">1285</span>
<span id="L1286" rel="#L1286">1286</span>
<span id="L1287" rel="#L1287">1287</span>
<span id="L1288" rel="#L1288">1288</span>
<span id="L1289" rel="#L1289">1289</span>
<span id="L1290" rel="#L1290">1290</span>
<span id="L1291" rel="#L1291">1291</span>
<span id="L1292" rel="#L1292">1292</span>
<span id="L1293" rel="#L1293">1293</span>
<span id="L1294" rel="#L1294">1294</span>
<span id="L1295" rel="#L1295">1295</span>
<span id="L1296" rel="#L1296">1296</span>
<span id="L1297" rel="#L1297">1297</span>
<span id="L1298" rel="#L1298">1298</span>
<span id="L1299" rel="#L1299">1299</span>
<span id="L1300" rel="#L1300">1300</span>
<span id="L1301" rel="#L1301">1301</span>
<span id="L1302" rel="#L1302">1302</span>
<span id="L1303" rel="#L1303">1303</span>
<span id="L1304" rel="#L1304">1304</span>
<span id="L1305" rel="#L1305">1305</span>
<span id="L1306" rel="#L1306">1306</span>
<span id="L1307" rel="#L1307">1307</span>
<span id="L1308" rel="#L1308">1308</span>
<span id="L1309" rel="#L1309">1309</span>
<span id="L1310" rel="#L1310">1310</span>
<span id="L1311" rel="#L1311">1311</span>
<span id="L1312" rel="#L1312">1312</span>
<span id="L1313" rel="#L1313">1313</span>
<span id="L1314" rel="#L1314">1314</span>
<span id="L1315" rel="#L1315">1315</span>
<span id="L1316" rel="#L1316">1316</span>
<span id="L1317" rel="#L1317">1317</span>
<span id="L1318" rel="#L1318">1318</span>
<span id="L1319" rel="#L1319">1319</span>
<span id="L1320" rel="#L1320">1320</span>
<span id="L1321" rel="#L1321">1321</span>
<span id="L1322" rel="#L1322">1322</span>
<span id="L1323" rel="#L1323">1323</span>
<span id="L1324" rel="#L1324">1324</span>
<span id="L1325" rel="#L1325">1325</span>
<span id="L1326" rel="#L1326">1326</span>
<span id="L1327" rel="#L1327">1327</span>
<span id="L1328" rel="#L1328">1328</span>
<span id="L1329" rel="#L1329">1329</span>
<span id="L1330" rel="#L1330">1330</span>
<span id="L1331" rel="#L1331">1331</span>
<span id="L1332" rel="#L1332">1332</span>
<span id="L1333" rel="#L1333">1333</span>
<span id="L1334" rel="#L1334">1334</span>
<span id="L1335" rel="#L1335">1335</span>
<span id="L1336" rel="#L1336">1336</span>
<span id="L1337" rel="#L1337">1337</span>
<span id="L1338" rel="#L1338">1338</span>
<span id="L1339" rel="#L1339">1339</span>
<span id="L1340" rel="#L1340">1340</span>
<span id="L1341" rel="#L1341">1341</span>
<span id="L1342" rel="#L1342">1342</span>
<span id="L1343" rel="#L1343">1343</span>
<span id="L1344" rel="#L1344">1344</span>
<span id="L1345" rel="#L1345">1345</span>
<span id="L1346" rel="#L1346">1346</span>
<span id="L1347" rel="#L1347">1347</span>
<span id="L1348" rel="#L1348">1348</span>
<span id="L1349" rel="#L1349">1349</span>

          </td>
          <td class="blob-line-code">
                  <div class="highlight"><pre><div class='line' id='LC1'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC2'><span class="k">class</span> <span class="nc">Window</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC3'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__new__</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">windowId</span><span class="o">=-</span><span class="mi">1</span><span class="p">):</span></div><div class='line' id='LC4'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Create a new Window to draw on.</span></div><div class='line' id='LC5'><br/></div><div class='line' id='LC6'><span class="sd">        Specify an id to use an existing window.</span></div><div class='line' id='LC7'><br/></div><div class='line' id='LC8'><span class="sd">        Raises:</span></div><div class='line' id='LC9'><span class="sd">            ValueError: If supplied window Id does not exist.</span></div><div class='line' id='LC10'><span class="sd">            Exception: If more then 200 windows are created.</span></div><div class='line' id='LC11'><br/></div><div class='line' id='LC12'><span class="sd">        Deleting this window will activate the old window that was active</span></div><div class='line' id='LC13'><span class="sd">        and resets (not delete) all controls that are associated with this window.</span></div><div class='line' id='LC14'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC15'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC16'><br/></div><div class='line' id='LC17'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">show</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC18'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Show this window.</span></div><div class='line' id='LC19'><br/></div><div class='line' id='LC20'><span class="sd">        Shows this window by activating it, calling close() after it wil activate the current window again.</span></div><div class='line' id='LC21'><br/></div><div class='line' id='LC22'><span class="sd">        Note:</span></div><div class='line' id='LC23'><span class="sd">            If your script ends this window will be closed to. To show it forever,</span></div><div class='line' id='LC24'><span class="sd">            make a loop at the end of your script and use doModal() instead.</span></div><div class='line' id='LC25'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC26'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC27'><br/></div><div class='line' id='LC28'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">close</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC29'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Closes this window.</span></div><div class='line' id='LC30'><br/></div><div class='line' id='LC31'><span class="sd">        Closes this window by activating the old window.</span></div><div class='line' id='LC32'><span class="sd">        The window is not deleted with this method.</span></div><div class='line' id='LC33'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC34'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC35'><br/></div><div class='line' id='LC36'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">onAction</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">):</span></div><div class='line' id='LC37'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;onAction method.</span></div><div class='line' id='LC38'><br/></div><div class='line' id='LC39'><span class="sd">        This method will recieve all actions that the main program will send to this window.</span></div><div class='line' id='LC40'><span class="sd">        By default, only the PREVIOUS_MENU action is handled.</span></div><div class='line' id='LC41'><span class="sd">        Overwrite this method to let your script handle all actions.</span></div><div class='line' id='LC42'><span class="sd">        Don&#39;t forget to capture ACTION_PREVIOUS_MENU, else the user can&#39;t close this window.</span></div><div class='line' id='LC43'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC44'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC45'><br/></div><div class='line' id='LC46'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">onClick</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">control</span><span class="p">):</span></div><div class='line' id='LC47'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;onClick method.</span></div><div class='line' id='LC48'><br/></div><div class='line' id='LC49'><span class="sd">        This method will recieve all click events that the main program will send to this window.</span></div><div class='line' id='LC50'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC51'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC52'><br/></div><div class='line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">onFocus</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">control</span><span class="p">):</span></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;onFocus method.</span></div><div class='line' id='LC55'><br/></div><div class='line' id='LC56'><span class="sd">        This method will recieve all focus events that the main program will send to this window.</span></div><div class='line' id='LC57'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC59'><br/></div><div class='line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">onInit</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC61'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;onInit method.</span></div><div class='line' id='LC62'><br/></div><div class='line' id='LC63'><span class="sd">        This method will be called to initialize the window.</span></div><div class='line' id='LC64'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC66'><br/></div><div class='line' id='LC67'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">doModal</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Display this window until close() is called.&quot;&quot;&quot;</span></div><div class='line' id='LC69'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC70'><br/></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">addControl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">Control</span><span class="p">):</span></div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Add a Control to this window.</span></div><div class='line' id='LC73'><br/></div><div class='line' id='LC74'><span class="sd">        Raises:</span></div><div class='line' id='LC75'><span class="sd">            TypeError: If supplied argument is not a Control type.</span></div><div class='line' id='LC76'><span class="sd">            ReferenceError: If control is already used in another window.</span></div><div class='line' id='LC77'><span class="sd">            RuntimeError: Should not happen :-)</span></div><div class='line' id='LC78'><br/></div><div class='line' id='LC79'><span class="sd">        The next controls can be added to a window atm:</span></div><div class='line' id='LC80'><span class="sd">            ControlLabel</span></div><div class='line' id='LC81'><span class="sd">            ControlFadeLabel</span></div><div class='line' id='LC82'><span class="sd">            ControlTextBox</span></div><div class='line' id='LC83'><span class="sd">            ControlButton</span></div><div class='line' id='LC84'><span class="sd">            ControlCheckMark</span></div><div class='line' id='LC85'><span class="sd">            ControlList</span></div><div class='line' id='LC86'><span class="sd">            ControlGroup</span></div><div class='line' id='LC87'><span class="sd">            ControlImage</span></div><div class='line' id='LC88'><span class="sd">            ControlRadioButton</span></div><div class='line' id='LC89'><span class="sd">            ControlProgress</span></div><div class='line' id='LC90'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC91'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC92'><br/></div><div class='line' id='LC93'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getControl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">controlId</span><span class="p">):</span></div><div class='line' id='LC94'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Get&#39;s the control from this window.</span></div><div class='line' id='LC95'><br/></div><div class='line' id='LC96'><span class="sd">        Raises:</span></div><div class='line' id='LC97'><span class="sd">            Exception: If Control doesn&#39;t exist</span></div><div class='line' id='LC98'><br/></div><div class='line' id='LC99'><span class="sd">        controlId doesn&#39;t have to be a python control, it can be a control id</span></div><div class='line' id='LC100'><span class="sd">        from a xbmc window too (you can find id&#39;s in the xml files).</span></div><div class='line' id='LC101'><br/></div><div class='line' id='LC102'><span class="sd">        Note:</span></div><div class='line' id='LC103'><span class="sd">            Not python controls are not completely usable yet.</span></div><div class='line' id='LC104'><span class="sd">            You can only use the Control functions.</span></div><div class='line' id='LC105'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">object</span></div><div class='line' id='LC107'><br/></div><div class='line' id='LC108'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setFocus</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">Control</span><span class="p">):</span></div><div class='line' id='LC109'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Give the supplied control focus.</span></div><div class='line' id='LC110'><br/></div><div class='line' id='LC111'><span class="sd">        Raises:</span></div><div class='line' id='LC112'><span class="sd">            TypeError: If supplied argument is not a Control type.</span></div><div class='line' id='LC113'><span class="sd">            SystemError: On Internal error.</span></div><div class='line' id='LC114'><span class="sd">            RuntimeError: If control is not added to a window.</span></div><div class='line' id='LC115'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC116'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC117'><br/></div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setFocusId</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span></div><div class='line' id='LC119'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Gives the control with the supplied focus.</span></div><div class='line' id='LC120'><br/></div><div class='line' id='LC121'><span class="sd">        Raises:</span></div><div class='line' id='LC122'><span class="sd">            SystemError: On Internal error.</span></div><div class='line' id='LC123'><span class="sd">            RuntimeError: If control is not added to a window.</span></div><div class='line' id='LC124'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC126'><br/></div><div class='line' id='LC127'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getFocus</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC128'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the control which is focused.</span></div><div class='line' id='LC129'><br/></div><div class='line' id='LC130'><span class="sd">        Raises:</span></div><div class='line' id='LC131'><span class="sd">            SystemError: On Internal error.</span></div><div class='line' id='LC132'><span class="sd">            RuntimeError: If no control has focus.</span></div><div class='line' id='LC133'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC134'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">object</span></div><div class='line' id='LC135'><br/></div><div class='line' id='LC136'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getFocusId</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC137'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the id of the control which is focused.</span></div><div class='line' id='LC138'><br/></div><div class='line' id='LC139'><span class="sd">        Raises:</span></div><div class='line' id='LC140'><span class="sd">            SystemError: On Internal error.</span></div><div class='line' id='LC141'><span class="sd">            RuntimeError: If no control has focus.</span></div><div class='line' id='LC142'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC143'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">long</span></div><div class='line' id='LC144'><br/></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">removeControl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">Control</span><span class="p">):</span></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Removes the control from this window.</span></div><div class='line' id='LC147'><br/></div><div class='line' id='LC148'><span class="sd">        Raises:</span></div><div class='line' id='LC149'><span class="sd">            TypeError: If supplied argument is not a Control type.</span></div><div class='line' id='LC150'><span class="sd">            RuntimeError: If control is not added to this window.</span></div><div class='line' id='LC151'><br/></div><div class='line' id='LC152'><span class="sd">        This will not delete the control. It is only removed from the window.</span></div><div class='line' id='LC153'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC154'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC155'><br/></div><div class='line' id='LC156'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getHeight</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC157'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the height of this screen.&quot;&quot;&quot;</span></div><div class='line' id='LC158'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">long</span></div><div class='line' id='LC159'><br/></div><div class='line' id='LC160'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getWidth</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC161'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the width of this screen.&quot;&quot;&quot;</span></div><div class='line' id='LC162'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">long</span></div><div class='line' id='LC163'><br/></div><div class='line' id='LC164'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getResolution</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC165'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the resolution of the screen.</span></div><div class='line' id='LC166'><br/></div><div class='line' id='LC167'><span class="sd">        The returned value is one of the following:</span></div><div class='line' id='LC168'><span class="sd">            0 - 1080i      (1920x1080)</span></div><div class='line' id='LC169'><span class="sd">            1 - 720p       (1280x720)</span></div><div class='line' id='LC170'><span class="sd">            2 - 480p 4:3   (720x480)</span></div><div class='line' id='LC171'><span class="sd">            3 - 480p 16:9  (720x480)</span></div><div class='line' id='LC172'><span class="sd">            4 - NTSC 4:3   (720x480)</span></div><div class='line' id='LC173'><span class="sd">            5 - NTSC 16:9  (720x480)</span></div><div class='line' id='LC174'><span class="sd">            6 - PAL 4:3    (720x576)</span></div><div class='line' id='LC175'><span class="sd">            7 - PAL 16:9   (720x576)</span></div><div class='line' id='LC176'><span class="sd">            8 - PAL60 4:3  (720x480)</span></div><div class='line' id='LC177'><span class="sd">            9 - PAL60 16:9 (720x480)</span></div><div class='line' id='LC178'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC179'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">long</span></div><div class='line' id='LC180'><br/></div><div class='line' id='LC181'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setCoordinateResolution</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">resolution</span><span class="p">):</span></div><div class='line' id='LC182'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Sets the resolution that the coordinates of all controls are defined in.</span></div><div class='line' id='LC183'><br/></div><div class='line' id='LC184'><span class="sd">        Allows XBMC to scale control positions and width/heights to whatever resolution</span></div><div class='line' id='LC185'><span class="sd">        XBMC is currently using.</span></div><div class='line' id='LC186'><br/></div><div class='line' id='LC187'><span class="sd">        resolution is one of the following:</span></div><div class='line' id='LC188'><span class="sd">            0 - 1080i      (1920x1080)</span></div><div class='line' id='LC189'><span class="sd">            1 - 720p       (1280x720)</span></div><div class='line' id='LC190'><span class="sd">            2 - 480p 4:3   (720x480)</span></div><div class='line' id='LC191'><span class="sd">            3 - 480p 16:9  (720x480)</span></div><div class='line' id='LC192'><span class="sd">            4 - NTSC 4:3   (720x480)</span></div><div class='line' id='LC193'><span class="sd">            5 - NTSC 16:9  (720x480)</span></div><div class='line' id='LC194'><span class="sd">            6 - PAL 4:3    (720x576)</span></div><div class='line' id='LC195'><span class="sd">            7 - PAL 16:9   (720x576)</span></div><div class='line' id='LC196'><span class="sd">            8 - PAL60 4:3  (720x480)</span></div><div class='line' id='LC197'><span class="sd">            9 - PAL60 16:9 (720x480)</span></div><div class='line' id='LC198'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC199'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC200'><br/></div><div class='line' id='LC201'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setProperty</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span></div><div class='line' id='LC202'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Sets a window property, similar to an infolabel.</span></div><div class='line' id='LC203'><br/></div><div class='line' id='LC204'><span class="sd">        key: string - property name.</span></div><div class='line' id='LC205'><span class="sd">        value: string or unicode - value of property.</span></div><div class='line' id='LC206'><br/></div><div class='line' id='LC207'><span class="sd">        Note:</span></div><div class='line' id='LC208'><span class="sd">            key is NOT case sensitive. Setting value to an empty string is equivalent to clearProperty(key).</span></div><div class='line' id='LC209'><br/></div><div class='line' id='LC210'><span class="sd">        Example:</span></div><div class='line' id='LC211'><span class="sd">            win = xbmcgui.Window(xbmcgui.getCurrentWindowId())</span></div><div class='line' id='LC212'><span class="sd">            win.setProperty(&#39;Category&#39;, &#39;Newest&#39;)</span></div><div class='line' id='LC213'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC214'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC215'><br/></div><div class='line' id='LC216'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getProperty</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">):</span></div><div class='line' id='LC217'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a window property as a string, similar to an infolabel.</span></div><div class='line' id='LC218'><br/></div><div class='line' id='LC219'><span class="sd">        key: string - property name.</span></div><div class='line' id='LC220'><br/></div><div class='line' id='LC221'><span class="sd">        Note:</span></div><div class='line' id='LC222'><span class="sd">            key is NOT case sensitive.</span></div><div class='line' id='LC223'><br/></div><div class='line' id='LC224'><span class="sd">        Example:</span></div><div class='line' id='LC225'><span class="sd">            win = xbmcgui.Window(xbmcgui.getCurrentWindowId())</span></div><div class='line' id='LC226'><span class="sd">            category = win.getProperty(&#39;Category&#39;)</span></div><div class='line' id='LC227'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC228'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC229'><br/></div><div class='line' id='LC230'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">clearProperty</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">):</span></div><div class='line' id='LC231'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Clears the specific window property.</span></div><div class='line' id='LC232'><br/></div><div class='line' id='LC233'><span class="sd">        key: string - property name.</span></div><div class='line' id='LC234'><br/></div><div class='line' id='LC235'><span class="sd">        Note:</span></div><div class='line' id='LC236'><span class="sd">            key is NOT case sensitive. Equivalent to setProperty(key,&#39;&#39;).</span></div><div class='line' id='LC237'><br/></div><div class='line' id='LC238'><span class="sd">        Example:</span></div><div class='line' id='LC239'><span class="sd">            win = xbmcgui.Window(xbmcgui.getCurrentWindowId())</span></div><div class='line' id='LC240'><span class="sd">            win.clearProperty(&#39;Category&#39;)</span></div><div class='line' id='LC241'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC242'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC243'><br/></div><div class='line' id='LC244'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">clearProperties</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC245'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Clears all window properties.</span></div><div class='line' id='LC246'><br/></div><div class='line' id='LC247'><span class="sd">        Example:</span></div><div class='line' id='LC248'><span class="sd">            win = xbmcgui.Window(xbmcgui.getCurrentWindowId())</span></div><div class='line' id='LC249'><span class="sd">            win.clearProperties()</span></div><div class='line' id='LC250'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC251'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC252'><br/></div><div class='line' id='LC253'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC254'><span class="k">class</span> <span class="nc">WindowDialog</span><span class="p">(</span><span class="n">Window</span><span class="p">):</span></div><div class='line' id='LC255'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__new__</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">xmlFilename</span><span class="p">,</span> <span class="n">scriptPath</span><span class="p">,</span> <span class="n">defaultSkin</span><span class="o">=</span><span class="s">&quot;Default&quot;</span><span class="p">,</span> <span class="n">defaultRes</span><span class="o">=</span><span class="s">&quot;720p&quot;</span><span class="p">):</span></div><div class='line' id='LC256'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Create a new WindowXMLDialog script.</span></div><div class='line' id='LC257'><br/></div><div class='line' id='LC258'><span class="sd">        xmlFilename: string - the name of the xml file to look for.</span></div><div class='line' id='LC259'><span class="sd">        scriptPath: string - path to script. used to fallback to if the xml doesn&#39;t exist in the current skin. (eg os.getcwd())</span></div><div class='line' id='LC260'><span class="sd">        defaultSkin: string - name of the folder in the skins path to look in for the xml.</span></div><div class='line' id='LC261'><span class="sd">        defaultRes: string - default skins resolution.</span></div><div class='line' id='LC262'><br/></div><div class='line' id='LC263'><span class="sd">        Note:</span></div><div class='line' id='LC264'><span class="sd">            Skin folder structure is eg(resources/skins/Default/720p).</span></div><div class='line' id='LC265'><br/></div><div class='line' id='LC266'><span class="sd">        Example:</span></div><div class='line' id='LC267'><span class="sd">            ui = GUI(&#39;script-Lyrics-main.xml&#39;, os.getcwd(), &#39;LCARS&#39;, &#39;PAL&#39;)</span></div><div class='line' id='LC268'><span class="sd">            ui.doModal()</span></div><div class='line' id='LC269'><span class="sd">            del ui</span></div><div class='line' id='LC270'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC271'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">super</span><span class="p">(</span><span class="n">WindowDialog</span><span class="p">,</span> <span class="n">cls</span><span class="p">)</span><span class="o">.</span><span class="n">__new__</span><span class="p">()</span></div><div class='line' id='LC272'><br/></div><div class='line' id='LC273'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC274'><span class="k">class</span> <span class="nc">WindowXML</span><span class="p">(</span><span class="n">Window</span><span class="p">):</span></div><div class='line' id='LC275'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__new__</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">xmlFilename</span><span class="p">,</span> <span class="n">scriptPath</span><span class="p">,</span> <span class="n">defaultSkin</span><span class="o">=</span><span class="s">&quot;Default&quot;</span><span class="p">,</span> <span class="n">defaultRes</span><span class="o">=</span><span class="s">&quot;720p&quot;</span><span class="p">):</span></div><div class='line' id='LC276'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Create a new WindowXML script.</span></div><div class='line' id='LC277'><br/></div><div class='line' id='LC278'><span class="sd">        xmlFilename: string - the name of the xml file to look for.</span></div><div class='line' id='LC279'><span class="sd">        scriptPath: string - path to script. used to fallback to if the xml doesn&#39;t exist in the current skin. (eg os.getcwd())</span></div><div class='line' id='LC280'><span class="sd">        defaultSkin: string - name of the folder in the skins path to look in for the xml.</span></div><div class='line' id='LC281'><span class="sd">        defaultRes: string - default skins resolution.</span></div><div class='line' id='LC282'><br/></div><div class='line' id='LC283'><span class="sd">        Note:</span></div><div class='line' id='LC284'><span class="sd">            Skin folder structure is eg(resources/skins/Default/720p).</span></div><div class='line' id='LC285'><br/></div><div class='line' id='LC286'><span class="sd">        Example:</span></div><div class='line' id='LC287'><span class="sd">            ui = GUI(&#39;script-Lyrics-main.xml&#39;, os.getcwd(), &#39;LCARS&#39;, &#39;PAL&#39;)</span></div><div class='line' id='LC288'><span class="sd">            ui.doModal()</span></div><div class='line' id='LC289'><span class="sd">            del ui</span></div><div class='line' id='LC290'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC291'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">super</span><span class="p">(</span><span class="n">WindowXML</span><span class="p">,</span> <span class="n">cls</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">()</span></div><div class='line' id='LC292'><br/></div><div class='line' id='LC293'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">removeItem</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">position</span><span class="p">):</span></div><div class='line' id='LC294'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Removes a specified item based on position, from the Window List.</span></div><div class='line' id='LC295'><br/></div><div class='line' id='LC296'><span class="sd">        position: integer - position of item to remove.</span></div><div class='line' id='LC297'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC298'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC299'><br/></div><div class='line' id='LC300'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">addItem</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item</span><span class="p">,</span> <span class="n">position</span><span class="o">=</span><span class="mi">32767</span><span class="p">):</span></div><div class='line' id='LC301'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Add a new item to this Window List.</span></div><div class='line' id='LC302'><br/></div><div class='line' id='LC303'><span class="sd">        item: string, unicode or ListItem - item to add.</span></div><div class='line' id='LC304'><span class="sd">        position: integer - position of item to add. (NO Int = Adds to bottom,0 adds to top, 1 adds to one below from top,-1 adds to one above from bottom etc etc)</span></div><div class='line' id='LC305'><span class="sd">                  If integer positions are greater than list size, negative positions will add to top of list, positive positions will add to bottom of list.</span></div><div class='line' id='LC306'><span class="sd">        Example:</span></div><div class='line' id='LC307'><span class="sd">            self.addItem(&#39;Reboot XBMC&#39;, 0)</span></div><div class='line' id='LC308'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC309'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC310'><br/></div><div class='line' id='LC311'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">clearList</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC312'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Clear the Window List.&quot;&quot;&quot;</span></div><div class='line' id='LC313'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC314'><br/></div><div class='line' id='LC315'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setCurrentListPosition</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">position</span><span class="p">):</span></div><div class='line' id='LC316'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Set the current position in the Window List.</span></div><div class='line' id='LC317'><br/></div><div class='line' id='LC318'><span class="sd">        position: integer - position of item to set.</span></div><div class='line' id='LC319'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC320'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC321'><br/></div><div class='line' id='LC322'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getCurrentListPosition</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC323'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Gets the current position in the Window List.&quot;&quot;&quot;</span></div><div class='line' id='LC324'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">long</span></div><div class='line' id='LC325'><br/></div><div class='line' id='LC326'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getListItem</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">position</span><span class="p">):</span></div><div class='line' id='LC327'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a given ListItem in this Window List.</span></div><div class='line' id='LC328'><br/></div><div class='line' id='LC329'><span class="sd">        position: integer - position of item to return.</span></div><div class='line' id='LC330'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC331'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">ListItem</span></div><div class='line' id='LC332'><br/></div><div class='line' id='LC333'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getListSize</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC334'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the number of items in this Window List.&quot;&quot;&quot;</span></div><div class='line' id='LC335'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">long</span></div><div class='line' id='LC336'><br/></div><div class='line' id='LC337'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setProperty</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span></div><div class='line' id='LC338'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Sets a container property, similar to an infolabel.</span></div><div class='line' id='LC339'><br/></div><div class='line' id='LC340'><span class="sd">        key: string - property name.</span></div><div class='line' id='LC341'><span class="sd">        value: string or unicode - value of property.</span></div><div class='line' id='LC342'><br/></div><div class='line' id='LC343'><span class="sd">        Note:</span></div><div class='line' id='LC344'><span class="sd">            Key is NOT case sensitive.</span></div><div class='line' id='LC345'><br/></div><div class='line' id='LC346'><span class="sd">        Example:</span></div><div class='line' id='LC347'><span class="sd">            self.setProperty(&#39;Category&#39;, &#39;Newest&#39;)</span></div><div class='line' id='LC348'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC349'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC350'><br/></div><div class='line' id='LC351'><br/></div><div class='line' id='LC352'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC353'><span class="k">class</span> <span class="nc">WindowXMLDialog</span><span class="p">(</span><span class="n">WindowXML</span><span class="p">):</span></div><div class='line' id='LC354'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__new__</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">xmlFilename</span><span class="p">,</span> <span class="n">scriptPath</span><span class="p">,</span> <span class="n">defaultSkin</span><span class="o">=</span><span class="s">&quot;Default&quot;</span><span class="p">,</span> <span class="n">defaultRes</span><span class="o">=</span><span class="s">&quot;720p&quot;</span><span class="p">):</span></div><div class='line' id='LC355'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Create a new WindowXMLDialog script.</span></div><div class='line' id='LC356'><br/></div><div class='line' id='LC357'><span class="sd">        xmlFilename: string - the name of the xml file to look for.</span></div><div class='line' id='LC358'><span class="sd">        scriptPath: string - path to script. used to fallback to if the xml doesn&#39;t exist in the current skin. (eg os.getcwd())</span></div><div class='line' id='LC359'><span class="sd">        defaultSkin: string - name of the folder in the skins path to look in for the xml.</span></div><div class='line' id='LC360'><span class="sd">        defaultRes: string - default skins resolution.</span></div><div class='line' id='LC361'><br/></div><div class='line' id='LC362'><span class="sd">        Note:</span></div><div class='line' id='LC363'><span class="sd">            Skin folder structure is eg(resources/skins/Default/720p).</span></div><div class='line' id='LC364'><br/></div><div class='line' id='LC365'><span class="sd">        Example:</span></div><div class='line' id='LC366'><span class="sd">            ui = GUI(&#39;script-Lyrics-main.xml&#39;, os.getcwd(), &#39;LCARS&#39;, &#39;PAL&#39;)</span></div><div class='line' id='LC367'><span class="sd">            ui.doModal()</span></div><div class='line' id='LC368'><span class="sd">            del ui</span></div><div class='line' id='LC369'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC370'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">super</span><span class="p">(</span><span class="n">WindowXML</span><span class="p">,</span> <span class="n">cls</span><span class="p">)</span><span class="o">.</span><span class="n">__new__</span><span class="p">()</span></div><div class='line' id='LC371'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC372'><br/></div><div class='line' id='LC373'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC374'><span class="k">class</span> <span class="nc">ListItem</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC375'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">label2</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">iconImage</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">thumbnailImage</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC376'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Creates a new ListItem.</span></div><div class='line' id='LC377'><br/></div><div class='line' id='LC378'><span class="sd">        label: string or unicode - label1 text.</span></div><div class='line' id='LC379'><span class="sd">        label2: string or unicode - label2 text.</span></div><div class='line' id='LC380'><span class="sd">        iconImage: string - icon filename.</span></div><div class='line' id='LC381'><span class="sd">        thumbnailImage: string - thumbnail filename.</span></div><div class='line' id='LC382'><span class="sd">        path: string or unicode - listitem&#39;s path.</span></div><div class='line' id='LC383'><br/></div><div class='line' id='LC384'><span class="sd">        Example:</span></div><div class='line' id='LC385'><span class="sd">            listitem = xbmcgui.ListItem(&#39;Casino Royale&#39;, &#39;[PG-13]&#39;, &#39;blank-poster.tbn&#39;, &#39;poster.tbn&#39;, path=&#39;f:\\movies\\casino_royale.mov&#39;)</span></div><div class='line' id='LC386'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC387'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC388'><br/></div><div class='line' id='LC389'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getLabel</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC390'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the listitem label.&quot;&quot;&quot;</span></div><div class='line' id='LC391'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC392'><br/></div><div class='line' id='LC393'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getLabel2</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC394'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the listitem&#39;s second label.&quot;&quot;&quot;</span></div><div class='line' id='LC395'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC396'><br/></div><div class='line' id='LC397'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setLabel</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">label</span><span class="p">):</span></div><div class='line' id='LC398'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Sets the listitem&#39;s label.</span></div><div class='line' id='LC399'><br/></div><div class='line' id='LC400'><span class="sd">        label: string or unicode - text string.</span></div><div class='line' id='LC401'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC402'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC403'><br/></div><div class='line' id='LC404'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setLabel2</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">label2</span><span class="p">):</span></div><div class='line' id='LC405'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Sets the listitem&#39;s second label.</span></div><div class='line' id='LC406'><br/></div><div class='line' id='LC407'><span class="sd">        label2: string or unicode - text string.</span></div><div class='line' id='LC408'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC409'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC410'><br/></div><div class='line' id='LC411'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setIconImage</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">icon</span><span class="p">):</span></div><div class='line' id='LC412'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Sets the listitem&#39;s icon image.</span></div><div class='line' id='LC413'><br/></div><div class='line' id='LC414'><span class="sd">        icon: string or unicode - image filename.</span></div><div class='line' id='LC415'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC416'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC417'><br/></div><div class='line' id='LC418'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setThumbnailImage</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">thumb</span><span class="p">):</span></div><div class='line' id='LC419'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Sets the listitem&#39;s thumbnail image.</span></div><div class='line' id='LC420'><br/></div><div class='line' id='LC421'><span class="sd">        thumb: string or unicode - image filename.</span></div><div class='line' id='LC422'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC423'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC424'><br/></div><div class='line' id='LC425'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">select</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">selected</span><span class="p">):</span></div><div class='line' id='LC426'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Sets the listitem&#39;s selected status.</span></div><div class='line' id='LC427'><br/></div><div class='line' id='LC428'><span class="sd">        selected: bool - True=selected/False=not selected.</span></div><div class='line' id='LC429'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC430'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC431'><br/></div><div class='line' id='LC432'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">isSelected</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC433'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the listitem&#39;s selected status.&quot;&quot;&quot;</span></div><div class='line' id='LC434'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">bool</span></div><div class='line' id='LC435'><br/></div><div class='line' id='LC436'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setInfo</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">type</span><span class="p">,</span> <span class="n">infoLabels</span><span class="p">):</span></div><div class='line' id='LC437'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Sets the listitem&#39;s infoLabels.</span></div><div class='line' id='LC438'><br/></div><div class='line' id='LC439'><span class="sd">        type: string - type of media(video/music/pictures).</span></div><div class='line' id='LC440'><span class="sd">        infoLabels: dictionary - pairs of { label: value }.</span></div><div class='line' id='LC441'><br/></div><div class='line' id='LC442'><span class="sd">        Note:</span></div><div class='line' id='LC443'><span class="sd">            To set pictures exif info, prepend &#39;exif:&#39; to the label. Exif values must be passed</span></div><div class='line' id='LC444'><span class="sd">            as strings, separate value pairs with a comma. (eg. {&#39;exif:resolution&#39;: &#39;720,480&#39;}</span></div><div class='line' id='LC445'><span class="sd">            See CPictureInfoTag::TranslateString in PictureInfoTag.cpp for valid strings.</span></div><div class='line' id='LC446'><br/></div><div class='line' id='LC447'><span class="sd">        General Values that apply to all types:</span></div><div class='line' id='LC448'><span class="sd">            count: integer (12) - can be used to store an id for later, or for sorting purposes</span></div><div class='line' id='LC449'><span class="sd">            size: long (1024) - size in bytes</span></div><div class='line' id='LC450'><span class="sd">            date: string (%d.%m.%Y / 01.01.2009) - file date</span></div><div class='line' id='LC451'><br/></div><div class='line' id='LC452'><span class="sd">        Video Values:</span></div><div class='line' id='LC453'><span class="sd">            genre: string (Comedy)</span></div><div class='line' id='LC454'><span class="sd">            year: integer (2009)</span></div><div class='line' id='LC455'><span class="sd">            episode: integer (4)</span></div><div class='line' id='LC456'><span class="sd">            season: integer (1)</span></div><div class='line' id='LC457'><span class="sd">            top250: integer (192)</span></div><div class='line' id='LC458'><span class="sd">            tracknumber: integer (3)</span></div><div class='line' id='LC459'><span class="sd">            rating: float (6.4) - range is 0..10</span></div><div class='line' id='LC460'><span class="sd">            watched: depreciated - use playcount instead</span></div><div class='line' id='LC461'><span class="sd">            playcount: integer (2) - number of times this item has been played</span></div><div class='line' id='LC462'><span class="sd">            overlay: integer (2) - range is 0..8.  See GUIListItem.h for values</span></div><div class='line' id='LC463'><span class="sd">            cast: list (Michal C. Hall)</span></div><div class='line' id='LC464'><span class="sd">            castandrole: list (Michael C. Hall|Dexter)</span></div><div class='line' id='LC465'><span class="sd">            director: string (Dagur Kari)</span></div><div class='line' id='LC466'><span class="sd">            mpaa: string (PG-13)</span></div><div class='line' id='LC467'><span class="sd">            plot: string (Long Description)</span></div><div class='line' id='LC468'><span class="sd">            plotoutline: string (Short Description)</span></div><div class='line' id='LC469'><span class="sd">            title: string (Big Fan)</span></div><div class='line' id='LC470'><span class="sd">            originaltitle: string (Big Fan)</span></div><div class='line' id='LC471'><span class="sd">            duration: string (3:18)</span></div><div class='line' id='LC472'><span class="sd">            studio: string (Warner Bros.)</span></div><div class='line' id='LC473'><span class="sd">            tagline: string (An awesome movie) - short description of movie</span></div><div class='line' id='LC474'><span class="sd">            writer: string (Robert D. Siegel)</span></div><div class='line' id='LC475'><span class="sd">            tvshowtitle: string (Heroes)</span></div><div class='line' id='LC476'><span class="sd">            premiered: string (2005-03-04)</span></div><div class='line' id='LC477'><span class="sd">            status: string (Continuing) - status of a TVshow</span></div><div class='line' id='LC478'><span class="sd">            code: string (tt0110293) - IMDb code</span></div><div class='line' id='LC479'><span class="sd">            aired: string (2008-12-07)</span></div><div class='line' id='LC480'><span class="sd">            credits: string (Andy Kaufman) - writing credits</span></div><div class='line' id='LC481'><span class="sd">            lastplayed: string (%Y-%m-%d %h:%m:%s = 2009-04-05 23:16:04)</span></div><div class='line' id='LC482'><span class="sd">            album: string (The Joshua Tree)</span></div><div class='line' id='LC483'><span class="sd">            votes: string (12345 votes)</span></div><div class='line' id='LC484'><span class="sd">            trailer: string (/home/user/trailer.avi)</span></div><div class='line' id='LC485'><br/></div><div class='line' id='LC486'><span class="sd">        Music Values:</span></div><div class='line' id='LC487'><span class="sd">            tracknumber: integer (8)</span></div><div class='line' id='LC488'><span class="sd">            duration: integer (245) - duration in seconds</span></div><div class='line' id='LC489'><span class="sd">            year: integer (1998)</span></div><div class='line' id='LC490'><span class="sd">            genre: string (Rock)</span></div><div class='line' id='LC491'><span class="sd">            album: string (Pulse)</span></div><div class='line' id='LC492'><span class="sd">            artist: string (Muse)</span></div><div class='line' id='LC493'><span class="sd">            title: string (American Pie)</span></div><div class='line' id='LC494'><span class="sd">            rating: string (3) - single character between 0 and 5</span></div><div class='line' id='LC495'><span class="sd">            lyrics: string (On a dark desert highway...)</span></div><div class='line' id='LC496'><span class="sd">            playcount: integer (2) - number of times this item has been played</span></div><div class='line' id='LC497'><span class="sd">            lastplayed: string (%Y-%m-%d %h:%m:%s = 2009-04-05 23:16:04)</span></div><div class='line' id='LC498'><br/></div><div class='line' id='LC499'><span class="sd">        Picture Values:</span></div><div class='line' id='LC500'><span class="sd">            title: string (In the last summer-1)</span></div><div class='line' id='LC501'><span class="sd">            picturepath: string (/home/username/pictures/img001.jpg)</span></div><div class='line' id='LC502'><span class="sd">            exif*: string (See CPictureInfoTag::TranslateString in PictureInfoTag.cpp for valid strings)</span></div><div class='line' id='LC503'><br/></div><div class='line' id='LC504'><span class="sd">        Example:</span></div><div class='line' id='LC505'><span class="sd">            self.list.getSelectedItem().setInfo(&#39;video&#39;, { &#39;Genre&#39;: &#39;Comedy&#39; })</span></div><div class='line' id='LC506'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC507'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC508'><br/></div><div class='line' id='LC509'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setProperty</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span></div><div class='line' id='LC510'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Sets a listitem property, similar to an infolabel.</span></div><div class='line' id='LC511'><br/></div><div class='line' id='LC512'><span class="sd">        key: string - property name.</span></div><div class='line' id='LC513'><span class="sd">        value: string or unicode - value of property.</span></div><div class='line' id='LC514'><br/></div><div class='line' id='LC515'><span class="sd">        Note:</span></div><div class='line' id='LC516'><span class="sd">            Key is NOT case sensitive.</span></div><div class='line' id='LC517'><br/></div><div class='line' id='LC518'><span class="sd">        Some of these are treated internally by XBMC, such as the &#39;StartOffset&#39; property, which is</span></div><div class='line' id='LC519'><span class="sd">        the offset in seconds at which to start playback of an item.  Others may be used in the skin</span></div><div class='line' id='LC520'><span class="sd">        to add extra information, such as &#39;WatchedCount&#39; for tvshow items</span></div><div class='line' id='LC521'><br/></div><div class='line' id='LC522'><span class="sd">        Example:</span></div><div class='line' id='LC523'><span class="sd">            self.list.getSelectedItem().setProperty(&#39;AspectRatio&#39;, &#39;1.85 : 1&#39;)</span></div><div class='line' id='LC524'><span class="sd">            self.list.getSelectedItem().setProperty(&#39;StartOffset&#39;, &#39;256.4&#39;)</span></div><div class='line' id='LC525'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC526'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC527'><br/></div><div class='line' id='LC528'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getProperty</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">):</span></div><div class='line' id='LC529'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a listitem property as a string, similar to an infolabel.</span></div><div class='line' id='LC530'><br/></div><div class='line' id='LC531'><span class="sd">        key: string - property name.</span></div><div class='line' id='LC532'><br/></div><div class='line' id='LC533'><span class="sd">        Note:</span></div><div class='line' id='LC534'><span class="sd">            Key is NOT case sensitive.</span></div><div class='line' id='LC535'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC536'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC537'><br/></div><div class='line' id='LC538'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">addContextMenuItems</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">list</span><span class="p">,</span> <span class="n">replaceItems</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span></div><div class='line' id='LC539'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Adds item(s) to the context menu for media lists.</span></div><div class='line' id='LC540'><br/></div><div class='line' id='LC541'><span class="sd">        items: list - [(label, action)] A list of tuples consisting of label and action pairs.</span></div><div class='line' id='LC542'><span class="sd">            label: string or unicode - item&#39;s label.</span></div><div class='line' id='LC543'><span class="sd">            action: string or unicode - any built-in function to perform.</span></div><div class='line' id='LC544'><span class="sd">        replaceItems: bool - True=only your items will show/False=your items will be added to context menu.</span></div><div class='line' id='LC545'><br/></div><div class='line' id='LC546'><span class="sd">        List of functions: http://wiki.xbmc.org/?title=List_of_Built_In_Functions</span></div><div class='line' id='LC547'><br/></div><div class='line' id='LC548'><span class="sd">        Example:</span></div><div class='line' id='LC549'><span class="sd">            listitem.addContextMenuItems([(&#39;Theater Showtimes&#39;, &#39;XBMC.RunScript(special://home/scripts/showtimes/default.py,Iron Man)&#39;)])</span></div><div class='line' id='LC550'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC551'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC552'><br/></div><div class='line' id='LC553'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setPath</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">):</span></div><div class='line' id='LC554'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Sets the listitem&#39;s path.</span></div><div class='line' id='LC555'><br/></div><div class='line' id='LC556'><span class="sd">        path: string or unicode - path, activated when item is clicked.</span></div><div class='line' id='LC557'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC558'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC559'><br/></div><div class='line' id='LC560'><br/></div><div class='line' id='LC561'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC562'><span class="k">class</span> <span class="nc">ControlLabel</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC563'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">width</span><span class="p">,</span> <span class="n">height</span><span class="p">,</span> <span class="n">label</span><span class="p">,</span> <span class="n">font</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">textColor</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">disabledColor</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">alignment</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></div><div class='line' id='LC564'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">hasPath</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">angle</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC565'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;ControlLabel class.</span></div><div class='line' id='LC566'><br/></div><div class='line' id='LC567'><span class="sd">        x: integer - x coordinate of control.</span></div><div class='line' id='LC568'><span class="sd">        y: integer - y coordinate of control.</span></div><div class='line' id='LC569'><span class="sd">        width: integer - width of control.</span></div><div class='line' id='LC570'><span class="sd">        height: integer - height of control.</span></div><div class='line' id='LC571'><span class="sd">        label: string or unicode - text string.</span></div><div class='line' id='LC572'><span class="sd">        font: string - font used for label text. (e.g. &#39;font13&#39;)</span></div><div class='line' id='LC573'><span class="sd">        textColor: hexstring - color of enabled label&#39;s label. (e.g. &#39;0xFFFFFFFF&#39;)</span></div><div class='line' id='LC574'><span class="sd">        disabledColor: hexstring - color of disabled label&#39;s label. (e.g. &#39;0xFFFF3300&#39;)</span></div><div class='line' id='LC575'><span class="sd">        alignment: integer - alignment of label - *Note, see xbfont.h</span></div><div class='line' id='LC576'><span class="sd">        hasPath: bool - True=stores a path / False=no path.</span></div><div class='line' id='LC577'><span class="sd">        angle: integer - angle of control. (+ rotates CCW, - rotates CW)&quot;</span></div><div class='line' id='LC578'><br/></div><div class='line' id='LC579'><span class="sd">        Note:</span></div><div class='line' id='LC580'><span class="sd">            After you create the control, you need to add it to the window with addControl().</span></div><div class='line' id='LC581'><br/></div><div class='line' id='LC582'><span class="sd">        Example:</span></div><div class='line' id='LC583'><span class="sd">            self.label = xbmcgui.ControlLabel(100, 250, 125, 75, &#39;Status&#39;, angle=45)</span></div><div class='line' id='LC584'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC585'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC586'><br/></div><div class='line' id='LC587'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setLabel</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">label</span><span class="p">):</span></div><div class='line' id='LC588'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Set&#39;s text for this label.</span></div><div class='line' id='LC589'><br/></div><div class='line' id='LC590'><span class="sd">        label: string or unicode - text string.</span></div><div class='line' id='LC591'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC592'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC593'><br/></div><div class='line' id='LC594'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getLabel</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC595'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the text value for this label.&quot;&quot;&quot;</span></div><div class='line' id='LC596'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC597'><br/></div><div class='line' id='LC598'><br/></div><div class='line' id='LC599'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC600'><span class="k">class</span> <span class="nc">ControlFadeLabel</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC601'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">width</span><span class="p">,</span> <span class="n">height</span><span class="p">,</span> <span class="n">font</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">textColor</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">alignment</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC602'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Control that scroll&#39;s lables.</span></div><div class='line' id='LC603'><br/></div><div class='line' id='LC604'><span class="sd">        x: integer - x coordinate of control.</span></div><div class='line' id='LC605'><span class="sd">        y: integer - y coordinate of control.</span></div><div class='line' id='LC606'><span class="sd">        width: integer - width of control.</span></div><div class='line' id='LC607'><span class="sd">        height: integer - height of control.</span></div><div class='line' id='LC608'><span class="sd">        font: string - font used for label text. (e.g. &#39;font13&#39;)</span></div><div class='line' id='LC609'><span class="sd">        textColor: hexstring - color of fadelabel&#39;s labels. (e.g. &#39;0xFFFFFFFF&#39;)</span></div><div class='line' id='LC610'><span class="sd">        alignment: integer - alignment of label - *Note, see xbfont.h</span></div><div class='line' id='LC611'><br/></div><div class='line' id='LC612'><span class="sd">        Note:</span></div><div class='line' id='LC613'><span class="sd">            After you create the control, you need to add it to the window with addControl().</span></div><div class='line' id='LC614'><br/></div><div class='line' id='LC615'><span class="sd">        Example:</span></div><div class='line' id='LC616'><span class="sd">            self.fadelabel = xbmcgui.ControlFadeLabel(100, 250, 200, 50, textColor=&#39;0xFFFFFFFF&#39;)</span></div><div class='line' id='LC617'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC618'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC619'><br/></div><div class='line' id='LC620'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">addLabel</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">label</span><span class="p">):</span></div><div class='line' id='LC621'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Add a label to this control for scrolling.</span></div><div class='line' id='LC622'><br/></div><div class='line' id='LC623'><span class="sd">        label: string or unicode - text string.</span></div><div class='line' id='LC624'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC625'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC626'><br/></div><div class='line' id='LC627'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC628'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Clears this fadelabel.&quot;&quot;&quot;</span></div><div class='line' id='LC629'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC630'><br/></div><div class='line' id='LC631'><br/></div><div class='line' id='LC632'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC633'><span class="k">class</span> <span class="nc">ControlTextBox</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC634'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">width</span><span class="p">,</span> <span class="n">height</span><span class="p">,</span> <span class="n">font</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">textColor</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC635'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;ControlTextBox class.</span></div><div class='line' id='LC636'><br/></div><div class='line' id='LC637'><span class="sd">        x: integer - x coordinate of control.</span></div><div class='line' id='LC638'><span class="sd">        y: integer - y coordinate of control.</span></div><div class='line' id='LC639'><span class="sd">        width: integer - width of control.</span></div><div class='line' id='LC640'><span class="sd">        height: integer - height of control.</span></div><div class='line' id='LC641'><span class="sd">        font: string - font used for text. (e.g. &#39;font13&#39;)</span></div><div class='line' id='LC642'><span class="sd">        textColor: hexstring - color of textbox&#39;s text. (e.g. &#39;0xFFFFFFFF&#39;)</span></div><div class='line' id='LC643'><br/></div><div class='line' id='LC644'><span class="sd">        Note:</span></div><div class='line' id='LC645'><span class="sd">            After you create the control, you need to add it to the window with addControl().</span></div><div class='line' id='LC646'><br/></div><div class='line' id='LC647'><span class="sd">        Example:</span></div><div class='line' id='LC648'><span class="sd">            self.textbox = xbmcgui.ControlTextBox(100, 250, 300, 300, textColor=&#39;0xFFFFFFFF&#39;)</span></div><div class='line' id='LC649'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC650'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC651'><br/></div><div class='line' id='LC652'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setText</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">):</span></div><div class='line' id='LC653'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Set&#39;s the text for this textbox.</span></div><div class='line' id='LC654'><br/></div><div class='line' id='LC655'><span class="sd">        text: string or unicode - text string.</span></div><div class='line' id='LC656'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC657'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC658'><br/></div><div class='line' id='LC659'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">scroll</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">position</span><span class="p">):</span></div><div class='line' id='LC660'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Scrolls to the given position.</span></div><div class='line' id='LC661'><br/></div><div class='line' id='LC662'><span class="sd">        id: integer - position to scroll to.</span></div><div class='line' id='LC663'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC664'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC665'><br/></div><div class='line' id='LC666'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC667'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Clear&#39;s this textbox.&quot;&quot;&quot;</span></div><div class='line' id='LC668'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC669'><br/></div><div class='line' id='LC670'><br/></div><div class='line' id='LC671'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC672'><span class="k">class</span> <span class="nc">ControlButton</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC673'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">width</span><span class="p">,</span> <span class="n">height</span><span class="p">,</span> <span class="n">label</span><span class="p">,</span> <span class="n">focusTexture</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">noFocusTexture</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">textOffsetX</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></div><div class='line' id='LC674'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">textOffsetY</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">alignment</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">font</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">textColor</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">disabledColor</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">angle</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></div><div class='line' id='LC675'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">shadowColor</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">focusedColor</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC676'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;ControlButton class.</span></div><div class='line' id='LC677'><br/></div><div class='line' id='LC678'><span class="sd">        x: integer - x coordinate of control.</span></div><div class='line' id='LC679'><span class="sd">        y: integer - y coordinate of control.</span></div><div class='line' id='LC680'><span class="sd">        width: integer - width of control.</span></div><div class='line' id='LC681'><span class="sd">        height: integer - height of control.</span></div><div class='line' id='LC682'><span class="sd">        label: string or unicode - text string.</span></div><div class='line' id='LC683'><span class="sd">        focusTexture: string - filename for focus texture.</span></div><div class='line' id='LC684'><span class="sd">        noFocusTexture: string - filename for no focus texture.</span></div><div class='line' id='LC685'><span class="sd">        textOffsetX: integer - x offset of label.</span></div><div class='line' id='LC686'><span class="sd">        textOffsetY: integer - y offset of label.</span></div><div class='line' id='LC687'><span class="sd">        alignment: integer - alignment of label - *Note, see xbfont.h</span></div><div class='line' id='LC688'><span class="sd">        font: string - font used for label text. (e.g. &#39;font13&#39;)</span></div><div class='line' id='LC689'><span class="sd">        textColor: hexstring - color of enabled button&#39;s label. (e.g. &#39;0xFFFFFFFF&#39;)</span></div><div class='line' id='LC690'><span class="sd">        disabledColor: hexstring - color of disabled button&#39;s label. (e.g. &#39;0xFFFF3300&#39;)</span></div><div class='line' id='LC691'><span class="sd">        angle: integer - angle of control. (+ rotates CCW, - rotates CW)</span></div><div class='line' id='LC692'><span class="sd">        shadowColor: hexstring - color of button&#39;s label&#39;s shadow. (e.g. &#39;0xFF000000&#39;)</span></div><div class='line' id='LC693'><span class="sd">        focusedColor: hexstring - color of focused button&#39;s label. (e.g. &#39;0xFF00FFFF&#39;)</span></div><div class='line' id='LC694'><br/></div><div class='line' id='LC695'><span class="sd">        Note:</span></div><div class='line' id='LC696'><span class="sd">            After you create the control, you need to add it to the window with addControl().</span></div><div class='line' id='LC697'><br/></div><div class='line' id='LC698'><span class="sd">        Example:</span></div><div class='line' id='LC699'><span class="sd">            self.button = xbmcgui.ControlButton(100, 250, 200, 50, &#39;Status&#39;, font=&#39;font14&#39;)</span></div><div class='line' id='LC700'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC701'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC702'><br/></div><div class='line' id='LC703'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setDisabledColor</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">disabledColor</span><span class="p">):</span></div><div class='line' id='LC704'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Set&#39;s this buttons disabled color.</span></div><div class='line' id='LC705'><br/></div><div class='line' id='LC706'><span class="sd">        disabledColor: hexstring - color of disabled button&#39;s label. (e.g. &#39;0xFFFF3300&#39;)</span></div><div class='line' id='LC707'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC708'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC709'><br/></div><div class='line' id='LC710'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setLabel</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">font</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">textColor</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">disabledColor</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">shadowColor</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">focusedColor</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC711'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Set&#39;s this buttons text attributes.</span></div><div class='line' id='LC712'><br/></div><div class='line' id='LC713'><span class="sd">        label: string or unicode - text string.</span></div><div class='line' id='LC714'><span class="sd">        font: string - font used for label text. (e.g. &#39;font13&#39;)</span></div><div class='line' id='LC715'><span class="sd">        textColor: hexstring - color of enabled button&#39;s label. (e.g. &#39;0xFFFFFFFF&#39;)</span></div><div class='line' id='LC716'><span class="sd">        disabledColor: hexstring - color of disabled button&#39;s label. (e.g. &#39;0xFFFF3300&#39;)</span></div><div class='line' id='LC717'><span class="sd">        shadowColor: hexstring - color of button&#39;s label&#39;s shadow. (e.g. &#39;0xFF000000&#39;)</span></div><div class='line' id='LC718'><span class="sd">        focusedColor: hexstring - color of focused button&#39;s label. (e.g. &#39;0xFFFFFF00&#39;)</span></div><div class='line' id='LC719'><span class="sd">        label2: string or unicode - text string.</span></div><div class='line' id='LC720'><br/></div><div class='line' id='LC721'><span class="sd">        Example:</span></div><div class='line' id='LC722'><span class="sd">            self.button.setLabel(&#39;Status&#39;, &#39;font14&#39;, &#39;0xFFFFFFFF&#39;, &#39;0xFFFF3300&#39;, &#39;0xFF000000&#39;)</span></div><div class='line' id='LC723'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC724'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC725'><br/></div><div class='line' id='LC726'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getLabel</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC727'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the buttons label as a unicode string.&quot;&quot;&quot;</span></div><div class='line' id='LC728'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">unicode</span></div><div class='line' id='LC729'><br/></div><div class='line' id='LC730'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getLabel2</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC731'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the buttons label2 as a unicode string.&quot;&quot;&quot;</span></div><div class='line' id='LC732'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">unicode</span></div><div class='line' id='LC733'><br/></div><div class='line' id='LC734'><br/></div><div class='line' id='LC735'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC736'><span class="k">class</span> <span class="nc">ControlCheckMark</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC737'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">width</span><span class="p">,</span> <span class="n">height</span><span class="p">,</span> <span class="n">label</span><span class="p">,</span> <span class="n">focusTexture</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">noFocusTexture</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">checkWidth</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></div><div class='line' id='LC738'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">checkHeight</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">alignment</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">font</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">textColor</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">disabledColor</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC739'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;ControlCheckMark class.</span></div><div class='line' id='LC740'><br/></div><div class='line' id='LC741'><span class="sd">        x: integer - x coordinate of control.</span></div><div class='line' id='LC742'><span class="sd">        y: integer - y coordinate of control.</span></div><div class='line' id='LC743'><span class="sd">        width: integer - width of control.</span></div><div class='line' id='LC744'><span class="sd">        height: integer - height of control.</span></div><div class='line' id='LC745'><span class="sd">        label: string or unicode - text string.</span></div><div class='line' id='LC746'><br/></div><div class='line' id='LC747'><span class="sd">        focusTexture: string - filename for focus texture.</span></div><div class='line' id='LC748'><span class="sd">        noFocusTexture: string - filename for no focus texture.</span></div><div class='line' id='LC749'><span class="sd">        checkWidth: integer - width of checkmark.</span></div><div class='line' id='LC750'><span class="sd">        checkHeight: integer - height of checkmark.</span></div><div class='line' id='LC751'><span class="sd">        alignment: integer - alignment of label - *Note, see xbfont.h</span></div><div class='line' id='LC752'><span class="sd">        font: string - font used for label text. (e.g. &#39;font13&#39;)</span></div><div class='line' id='LC753'><span class="sd">        textColor: hexstring - color of enabled checkmark&#39;s label. (e.g. &#39;0xFFFFFFFF&#39;)</span></div><div class='line' id='LC754'><span class="sd">        disabledColor: hexstring - color of disabled checkmark&#39;s label. (e.g. &#39;0xFFFF3300&#39;)</span></div><div class='line' id='LC755'><br/></div><div class='line' id='LC756'><span class="sd">        Note:</span></div><div class='line' id='LC757'><span class="sd">            After you create the control, you need to add it to the window with addControl().</span></div><div class='line' id='LC758'><br/></div><div class='line' id='LC759'><span class="sd">        Example:</span></div><div class='line' id='LC760'><span class="sd">            self.checkmark = xbmcgui.ControlCheckMark(100, 250, 200, 50, &#39;Status&#39;, font=&#39;font14&#39;)</span></div><div class='line' id='LC761'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC762'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC763'><br/></div><div class='line' id='LC764'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setDisabledColor</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">disabledColor</span><span class="p">):</span></div><div class='line' id='LC765'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Set&#39;s this controls disabled color.</span></div><div class='line' id='LC766'><br/></div><div class='line' id='LC767'><span class="sd">        disabledColor: hexstring - color of disabled checkmark&#39;s label. (e.g. &#39;0xFFFF3300&#39;)</span></div><div class='line' id='LC768'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC769'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC770'><br/></div><div class='line' id='LC771'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setLabel</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">label</span><span class="p">,</span> <span class="n">font</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">textColor</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">disabledColor</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC772'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Set&#39;s this controls text attributes.</span></div><div class='line' id='LC773'><br/></div><div class='line' id='LC774'><span class="sd">        label: string or unicode - text string.</span></div><div class='line' id='LC775'><span class="sd">        font: string - font used for label text. (e.g. &#39;font13&#39;)</span></div><div class='line' id='LC776'><span class="sd">        textColor: hexstring - color of enabled checkmark&#39;s label. (e.g. &#39;0xFFFFFFFF&#39;)</span></div><div class='line' id='LC777'><span class="sd">        disabledColor: hexstring - color of disabled checkmark&#39;s label. (e.g. &#39;0xFFFF3300&#39;)</span></div><div class='line' id='LC778'><br/></div><div class='line' id='LC779'><span class="sd">        Example:</span></div><div class='line' id='LC780'><span class="sd">            self.checkmark.setLabel(&#39;Status&#39;, &#39;font14&#39;, &#39;0xFFFFFFFF&#39;, &#39;0xFFFF3300&#39;)</span></div><div class='line' id='LC781'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC782'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC783'><br/></div><div class='line' id='LC784'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getSelected</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC785'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the selected status for this checkmark as a bool.&quot;&quot;&quot;</span></div><div class='line' id='LC786'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">bool</span></div><div class='line' id='LC787'><br/></div><div class='line' id='LC788'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setSelected</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">isOn</span><span class="p">):</span></div><div class='line' id='LC789'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Sets this checkmark status to on or off.</span></div><div class='line' id='LC790'><br/></div><div class='line' id='LC791'><span class="sd">        isOn: bool - True=selected (on) / False=not selected (off)</span></div><div class='line' id='LC792'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC793'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC794'><br/></div><div class='line' id='LC795'><br/></div><div class='line' id='LC796'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC797'><span class="k">class</span> <span class="nc">ControlList</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC798'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">width</span><span class="p">,</span> <span class="n">height</span><span class="p">,</span> <span class="n">font</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">textColor</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">buttonTexture</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">buttonFocusTexture</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></div><div class='line' id='LC799'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">selectedColor</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">imageWidth</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">imageHeight</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">itemTextXOffset</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">itemTextYOffset</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></div><div class='line' id='LC800'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">itemHeight</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">space</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">alignmentY</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC801'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;ControlList class.</span></div><div class='line' id='LC802'><br/></div><div class='line' id='LC803'><span class="sd">        x: integer - x coordinate of control.</span></div><div class='line' id='LC804'><span class="sd">        y: integer - y coordinate of control.</span></div><div class='line' id='LC805'><span class="sd">        width: integer - width of control.</span></div><div class='line' id='LC806'><span class="sd">        height: integer - height of control.</span></div><div class='line' id='LC807'><span class="sd">        font: string - font used for items label. (e.g. &#39;font13&#39;)</span></div><div class='line' id='LC808'><span class="sd">        textColor: hexstring - color of items label. (e.g. &#39;0xFFFFFFFF&#39;)</span></div><div class='line' id='LC809'><span class="sd">        buttonTexture: string - filename for focus texture.</span></div><div class='line' id='LC810'><span class="sd">        buttonFocusTexture: string - filename for no focus texture.</span></div><div class='line' id='LC811'><span class="sd">        selectedColor: integer - x offset of label.</span></div><div class='line' id='LC812'><span class="sd">        imageWidth: integer - width of items icon or thumbnail.</span></div><div class='line' id='LC813'><span class="sd">        imageHeight: integer - height of items icon or thumbnail.</span></div><div class='line' id='LC814'><span class="sd">        itemTextXOffset: integer - x offset of items label.</span></div><div class='line' id='LC815'><span class="sd">        itemTextYOffset: integer - y offset of items label.</span></div><div class='line' id='LC816'><span class="sd">        itemHeight: integer - height of items.</span></div><div class='line' id='LC817'><span class="sd">        space: integer - space between items.</span></div><div class='line' id='LC818'><span class="sd">        alignmentY: integer - Y-axis alignment of items label - *Note, see xbfont.h</span></div><div class='line' id='LC819'><br/></div><div class='line' id='LC820'><span class="sd">        Note:</span></div><div class='line' id='LC821'><span class="sd">            After you create the control, you need to add it to the window with addControl().</span></div><div class='line' id='LC822'><br/></div><div class='line' id='LC823'><span class="sd">        Example:</span></div><div class='line' id='LC824'><span class="sd">            self.cList = xbmcgui.ControlList(100, 250, 200, 250, &#39;font14&#39;, space=5)</span></div><div class='line' id='LC825'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC826'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC827'><br/></div><div class='line' id='LC828'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">addItem</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item</span><span class="p">):</span></div><div class='line' id='LC829'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Add a new item to this list control.</span></div><div class='line' id='LC830'><br/></div><div class='line' id='LC831'><span class="sd">        item: string, unicode or ListItem - item to add.</span></div><div class='line' id='LC832'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC833'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC834'><br/></div><div class='line' id='LC835'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">addItems</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">items</span><span class="p">):</span></div><div class='line' id='LC836'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Adds a list of listitems or strings to this list control.</span></div><div class='line' id='LC837'><br/></div><div class='line' id='LC838'><span class="sd">        items: List - list of strings, unicode objects or ListItems to add.</span></div><div class='line' id='LC839'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC840'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC841'><br/></div><div class='line' id='LC842'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">selectItem</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item</span><span class="p">):</span></div><div class='line' id='LC843'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Select an item by index number.</span></div><div class='line' id='LC844'><br/></div><div class='line' id='LC845'><span class="sd">        item: integer - index number of the item to select.</span></div><div class='line' id='LC846'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC847'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC848'><br/></div><div class='line' id='LC849'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC850'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Clear all ListItems in this control list.&quot;&quot;&quot;</span></div><div class='line' id='LC851'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC852'><br/></div><div class='line' id='LC853'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getSpinControl</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC854'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the associated ControlSpin object.</span></div><div class='line' id='LC855'><br/></div><div class='line' id='LC856'><span class="sd">        Note:</span></div><div class='line' id='LC857'><span class="sd">            Not working completely yet -</span></div><div class='line' id='LC858'><span class="sd">            After adding this control list to a window it is not possible to change</span></div><div class='line' id='LC859'><span class="sd">            the settings of this spin control.</span></div><div class='line' id='LC860'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC861'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">object</span></div><div class='line' id='LC862'><br/></div><div class='line' id='LC863'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setImageDimensions</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">imageWidth</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">imageHeight</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC864'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Sets the width/height of items icon or thumbnail.</span></div><div class='line' id='LC865'><br/></div><div class='line' id='LC866'><span class="sd">        imageWidth: integer - width of items icon or thumbnail.</span></div><div class='line' id='LC867'><span class="sd">        imageHeight: integer - height of items icon or thumbnail.</span></div><div class='line' id='LC868'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC869'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC870'><br/></div><div class='line' id='LC871'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setItemHeight</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">itemHeight</span><span class="p">):</span></div><div class='line' id='LC872'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Sets the height of items.</span></div><div class='line' id='LC873'><br/></div><div class='line' id='LC874'><span class="sd">        itemHeight: integer - height of items.</span></div><div class='line' id='LC875'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC876'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC877'><br/></div><div class='line' id='LC878'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setPageControlVisible</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">visible</span><span class="p">):</span></div><div class='line' id='LC879'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Sets the spin control&#39;s visible/hidden state.</span></div><div class='line' id='LC880'><br/></div><div class='line' id='LC881'><span class="sd">        visible: boolean - True=visible / False=hidden.</span></div><div class='line' id='LC882'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC883'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC884'><br/></div><div class='line' id='LC885'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setSpace</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">space</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC886'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Set&#39;s the space between items.</span></div><div class='line' id='LC887'><br/></div><div class='line' id='LC888'><span class="sd">        space: integer - space between items.</span></div><div class='line' id='LC889'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC890'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC891'><br/></div><div class='line' id='LC892'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getSelectedPosition</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC893'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the position of the selected item as an integer.</span></div><div class='line' id='LC894'><br/></div><div class='line' id='LC895'><span class="sd">        Note:</span></div><div class='line' id='LC896'><span class="sd">            Returns -1 for empty lists.</span></div><div class='line' id='LC897'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC898'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">long</span></div><div class='line' id='LC899'><br/></div><div class='line' id='LC900'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getSelectedItem</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC901'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the selected item as a ListItem object.</span></div><div class='line' id='LC902'><br/></div><div class='line' id='LC903'><span class="sd">        Note:</span></div><div class='line' id='LC904'><span class="sd">            Same as getSelectedPosition(), but instead of an integer a ListItem object is returned. Returns None for empty lists.</span></div><div class='line' id='LC905'><span class="sd">            See windowexample.py on how to use this.</span></div><div class='line' id='LC906'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC907'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">ListItem</span></div><div class='line' id='LC908'><br/></div><div class='line' id='LC909'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">size</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC910'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the total number of items in this list control as an integer.&quot;&quot;&quot;</span></div><div class='line' id='LC911'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">long</span></div><div class='line' id='LC912'><br/></div><div class='line' id='LC913'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getListItem</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index</span><span class="p">):</span></div><div class='line' id='LC914'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a given ListItem in this List.</span></div><div class='line' id='LC915'><br/></div><div class='line' id='LC916'><span class="sd">        index: integer - index number of item to return.</span></div><div class='line' id='LC917'><br/></div><div class='line' id='LC918'><span class="sd">        Raises:</span></div><div class='line' id='LC919'><span class="sd">            ValueError: If index is out of range.</span></div><div class='line' id='LC920'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC921'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">ListItem</span></div><div class='line' id='LC922'><br/></div><div class='line' id='LC923'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getItemHeight</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC924'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the control&#39;s current item height as an integer.&quot;&quot;&quot;</span></div><div class='line' id='LC925'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">long</span></div><div class='line' id='LC926'><br/></div><div class='line' id='LC927'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getSpace</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC928'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the control&#39;s space between items as an integer.&quot;&quot;&quot;</span></div><div class='line' id='LC929'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">long</span></div><div class='line' id='LC930'><br/></div><div class='line' id='LC931'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setStaticContent</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">items</span><span class="p">):</span></div><div class='line' id='LC932'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Fills a static list with a list of listitems.</span></div><div class='line' id='LC933'><br/></div><div class='line' id='LC934'><span class="sd">        items: List - list of listitems to add.</span></div><div class='line' id='LC935'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC936'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC937'><br/></div><div class='line' id='LC938'><br/></div><div class='line' id='LC939'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC940'><span class="k">class</span> <span class="nc">ControlImage</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC941'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">width</span><span class="p">,</span> <span class="n">height</span><span class="p">,</span> <span class="n">filename</span><span class="p">,</span> <span class="n">colorKey</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">aspectRatio</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">colorDiffuse</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC942'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;ControlImage class.</span></div><div class='line' id='LC943'><br/></div><div class='line' id='LC944'><span class="sd">        x: integer - x coordinate of control.</span></div><div class='line' id='LC945'><span class="sd">        y: integer - y coordinate of control.</span></div><div class='line' id='LC946'><span class="sd">        width: integer - width of control.</span></div><div class='line' id='LC947'><span class="sd">        height: integer - height of control.</span></div><div class='line' id='LC948'><span class="sd">        filename: string - image filename.</span></div><div class='line' id='LC949'><span class="sd">        colorKey: hexString - (example, &#39;0xFFFF3300&#39;)</span></div><div class='line' id='LC950'><span class="sd">        aspectRatio: integer - (values 0 = stretch (default), 1 = scale up (crops), 2 = scale down (black bars)</span></div><div class='line' id='LC951'><span class="sd">        colorDiffuse: hexString - (example, &#39;0xC0FF0000&#39; (red tint)).</span></div><div class='line' id='LC952'><br/></div><div class='line' id='LC953'><span class="sd">        Note:</span></div><div class='line' id='LC954'><span class="sd">            After you create the control, you need to add it to the window with addControl().</span></div><div class='line' id='LC955'><br/></div><div class='line' id='LC956'><span class="sd">        Example:</span></div><div class='line' id='LC957'><span class="sd">            self.image = xbmcgui.ControlImage(100, 250, 125, 75, aspectRatio=2)</span></div><div class='line' id='LC958'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC959'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC960'><br/></div><div class='line' id='LC961'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setImage</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">filename</span><span class="p">):</span></div><div class='line' id='LC962'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Changes the image.</span></div><div class='line' id='LC963'><br/></div><div class='line' id='LC964'><span class="sd">        filename: string - image filename.</span></div><div class='line' id='LC965'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC966'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC967'><br/></div><div class='line' id='LC968'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setColorDiffuse</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">colorDiffuse</span><span class="p">):</span></div><div class='line' id='LC969'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Changes the images color.</span></div><div class='line' id='LC970'><br/></div><div class='line' id='LC971'><span class="sd">        colorDiffuse: hexString - (example, &#39;0xC0FF0000&#39; (red tint)).</span></div><div class='line' id='LC972'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC973'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC974'><br/></div><div class='line' id='LC975'><br/></div><div class='line' id='LC976'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC977'><span class="k">class</span> <span class="nc">ControlProgress</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC978'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">width</span><span class="p">,</span> <span class="n">height</span><span class="p">,</span> <span class="n">texturebg</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">textureleft</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">texturemid</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">textureright</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></div><div class='line' id='LC979'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">textureoverlay</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC980'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;ControlProgress class.</span></div><div class='line' id='LC981'><br/></div><div class='line' id='LC982'><span class="sd">        x: integer - x coordinate of control.</span></div><div class='line' id='LC983'><span class="sd">        y: integer - y coordinate of control.</span></div><div class='line' id='LC984'><span class="sd">        width: integer - width of control.</span></div><div class='line' id='LC985'><span class="sd">        height: integer - height of control.</span></div><div class='line' id='LC986'><span class="sd">        texturebg: string - image filename.</span></div><div class='line' id='LC987'><span class="sd">        textureleft: string - image filename.</span></div><div class='line' id='LC988'><span class="sd">        texturemid: string - image filename.</span></div><div class='line' id='LC989'><span class="sd">        textureright: string - image filename.</span></div><div class='line' id='LC990'><span class="sd">        textureoverlay: string - image filename.</span></div><div class='line' id='LC991'><br/></div><div class='line' id='LC992'><span class="sd">        Note:</span></div><div class='line' id='LC993'><span class="sd">            After you create the control, you need to add it to the window with addControl().</span></div><div class='line' id='LC994'><br/></div><div class='line' id='LC995'><span class="sd">        Example:</span></div><div class='line' id='LC996'><span class="sd">            self.progress = xbmcgui.ControlProgress(100, 250, 125, 75)</span></div><div class='line' id='LC997'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC998'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC999'><br/></div><div class='line' id='LC1000'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setPercent</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">percent</span><span class="p">):</span></div><div class='line' id='LC1001'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Sets the percentage of the progressbar to show.</span></div><div class='line' id='LC1002'><br/></div><div class='line' id='LC1003'><span class="sd">        percent: float - percentage of the bar to show.</span></div><div class='line' id='LC1004'><br/></div><div class='line' id='LC1005'><span class="sd">        Note:</span></div><div class='line' id='LC1006'><span class="sd">            Valid range for percent is 0-100.</span></div><div class='line' id='LC1007'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC1008'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC1009'><br/></div><div class='line' id='LC1010'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getPercent</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC1011'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a float of the percent of the progress.&quot;&quot;&quot;</span></div><div class='line' id='LC1012'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">float</span></div><div class='line' id='LC1013'><br/></div><div class='line' id='LC1014'><br/></div><div class='line' id='LC1015'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC1016'><span class="k">class</span> <span class="nc">ControlSlider</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC1017'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">width</span><span class="p">,</span> <span class="n">height</span><span class="p">,</span> <span class="n">textureback</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">texture</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">texturefocus</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC1018'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;ControlSlider class.</span></div><div class='line' id='LC1019'><br/></div><div class='line' id='LC1020'><span class="sd">        x: integer - x coordinate of control.</span></div><div class='line' id='LC1021'><span class="sd">        y: integer - y coordinate of control.</span></div><div class='line' id='LC1022'><span class="sd">        width: integer - width of control.</span></div><div class='line' id='LC1023'><span class="sd">        height: integer - height of control.</span></div><div class='line' id='LC1024'><span class="sd">        textureback: string - image filename.</span></div><div class='line' id='LC1025'><span class="sd">        texture: string - image filename.</span></div><div class='line' id='LC1026'><span class="sd">        texturefocus: string - image filename.</span></div><div class='line' id='LC1027'><br/></div><div class='line' id='LC1028'><span class="sd">        Note:</span></div><div class='line' id='LC1029'><span class="sd">            After you create the control, you need to add it to the window with addControl().</span></div><div class='line' id='LC1030'><br/></div><div class='line' id='LC1031'><span class="sd">        Example:</span></div><div class='line' id='LC1032'><span class="sd">            self.slider = xbmcgui.ControlSlider(100, 250, 350, 40)</span></div><div class='line' id='LC1033'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC1034'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC1035'><br/></div><div class='line' id='LC1036'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getPercent</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC1037'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a float of the percent of the slider.&quot;&quot;&quot;</span></div><div class='line' id='LC1038'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">float</span></div><div class='line' id='LC1039'><br/></div><div class='line' id='LC1040'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setPercent</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">percent</span><span class="p">):</span></div><div class='line' id='LC1041'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Sets the percent of the slider.&quot;&quot;&quot;</span></div><div class='line' id='LC1042'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC1043'><br/></div><div class='line' id='LC1044'><br/></div><div class='line' id='LC1045'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC1046'><span class="k">class</span> <span class="nc">ControlGroup</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC1047'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC1048'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;ControlGroup class.</span></div><div class='line' id='LC1049'><br/></div><div class='line' id='LC1050'><span class="sd">        x: integer - x coordinate of control.</span></div><div class='line' id='LC1051'><span class="sd">        y: integer - y coordinate of control.</span></div><div class='line' id='LC1052'><span class="sd">        width: integer - width of control.</span></div><div class='line' id='LC1053'><span class="sd">        height: integer - height of control.</span></div><div class='line' id='LC1054'><br/></div><div class='line' id='LC1055'><span class="sd">        Example:</span></div><div class='line' id='LC1056'><span class="sd">            self.group = xbmcgui.ControlGroup(100, 250, 125, 75)</span></div><div class='line' id='LC1057'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC1058'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC1059'><br/></div><div class='line' id='LC1060'><br/></div><div class='line' id='LC1061'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC1062'><span class="k">class</span> <span class="nc">Dialog</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC1063'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">ok</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">heading</span><span class="p">,</span> <span class="n">line1</span><span class="p">,</span> <span class="n">line2</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">line3</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC1064'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Show a dialog &#39;OK&#39;.</span></div><div class='line' id='LC1065'><br/></div><div class='line' id='LC1066'><span class="sd">        heading: string or unicode - dialog heading.</span></div><div class='line' id='LC1067'><span class="sd">        line1: string or unicode - line #1 text.</span></div><div class='line' id='LC1068'><span class="sd">        line2: string or unicode - line #2 text.</span></div><div class='line' id='LC1069'><span class="sd">        line3: string or unicode - line #3 text.</span></div><div class='line' id='LC1070'><br/></div><div class='line' id='LC1071'><span class="sd">        Note:</span></div><div class='line' id='LC1072'><span class="sd">            Returns True if &#39;Ok&#39; was pressed, else False.</span></div><div class='line' id='LC1073'><br/></div><div class='line' id='LC1074'><span class="sd">        Example:</span></div><div class='line' id='LC1075'><span class="sd">            dialog = xbmcgui.Dialog()</span></div><div class='line' id='LC1076'><span class="sd">            ok = dialog.ok(&#39;XBMC&#39;, &#39;There was an error.&#39;)</span></div><div class='line' id='LC1077'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC1078'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">bool</span></div><div class='line' id='LC1079'><br/></div><div class='line' id='LC1080'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">browse</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">type</span><span class="p">,</span> <span class="n">heading</span><span class="p">,</span> <span class="n">shares</span><span class="p">,</span> <span class="n">mask</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">useThumbs</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">treatAsFolder</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></div><div class='line' id='LC1081'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">enableMultiple</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span></div><div class='line' id='LC1082'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Show a &#39;Browse&#39; dialog.</span></div><div class='line' id='LC1083'><br/></div><div class='line' id='LC1084'><span class="sd">        type: integer - the type of browse dialog.</span></div><div class='line' id='LC1085'><span class="sd">        heading: string or unicode - dialog heading.</span></div><div class='line' id='LC1086'><span class="sd">        shares: string or unicode - from sources.xml. (i.e. &#39;myprograms&#39;)</span></div><div class='line' id='LC1087'><span class="sd">        mask: string or unicode - &#39;|&#39; separated file mask. (i.e. &#39;.jpg|.png&#39;)</span></div><div class='line' id='LC1088'><span class="sd">        useThumbs: boolean - if True autoswitch to Thumb view if files exist.</span></div><div class='line' id='LC1089'><span class="sd">        treatAsFolder: boolean - if True playlists and archives act as folders.</span></div><div class='line' id='LC1090'><span class="sd">        default: string - default path or file.</span></div><div class='line' id='LC1091'><span class="sd">        enableMultiple: boolean - if True multiple file selection is enabled.</span></div><div class='line' id='LC1092'><br/></div><div class='line' id='LC1093'><span class="sd">        Types:</span></div><div class='line' id='LC1094'><span class="sd">            0: ShowAndGetDirectory</span></div><div class='line' id='LC1095'><span class="sd">            1: ShowAndGetFile</span></div><div class='line' id='LC1096'><span class="sd">            2: ShowAndGetImage</span></div><div class='line' id='LC1097'><span class="sd">            3: ShowAndGetWriteableDirectory</span></div><div class='line' id='LC1098'><br/></div><div class='line' id='LC1099'><span class="sd">        Note:</span></div><div class='line' id='LC1100'><span class="sd">            If enableMultiple is False (default): returns filename and/or path as a string</span></div><div class='line' id='LC1101'><span class="sd">            to the location of the highlighted item, if user pressed &#39;Ok&#39; or a masked item</span></div><div class='line' id='LC1102'><span class="sd">            was selected. Returns the default value if dialog was canceled.</span></div><div class='line' id='LC1103'><span class="sd">            If enableMultiple is True: returns tuple of marked filenames as a string,</span></div><div class='line' id='LC1104'><span class="sd">            if user pressed &#39;Ok&#39; or a masked item was selected. Returns empty tuple if dialog was canceled.</span></div><div class='line' id='LC1105'><br/></div><div class='line' id='LC1106'><span class="sd">            If type is 0 or 3 the enableMultiple parameter is ignored.</span></div><div class='line' id='LC1107'><br/></div><div class='line' id='LC1108'><span class="sd">        Example:</span></div><div class='line' id='LC1109'><span class="sd">            dialog = xbmcgui.Dialog()</span></div><div class='line' id='LC1110'><span class="sd">            fn = dialog.browse(3, &#39;XBMC&#39;, &#39;files&#39;, &#39;&#39;, False, False, False, &#39;special://masterprofile/script_data/XBMC Lyrics&#39;)</span></div><div class='line' id='LC1111'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC1112'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC1113'><br/></div><div class='line' id='LC1114'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">numeric</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">type</span><span class="p">,</span> <span class="n">heading</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC1115'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Show a &#39;Numeric&#39; dialog.</span></div><div class='line' id='LC1116'><br/></div><div class='line' id='LC1117'><span class="sd">        type: integer - the type of numeric dialog.</span></div><div class='line' id='LC1118'><span class="sd">        heading: string or unicode - dialog heading.</span></div><div class='line' id='LC1119'><span class="sd">        default: string - default value.</span></div><div class='line' id='LC1120'><br/></div><div class='line' id='LC1121'><span class="sd">        Types:</span></div><div class='line' id='LC1122'><span class="sd">            0: ShowAndGetNumber    (default format: #)</span></div><div class='line' id='LC1123'><span class="sd">            1: ShowAndGetDate      (default format: DD/MM/YYYY)</span></div><div class='line' id='LC1124'><span class="sd">            2: ShowAndGetTime      (default format: HH:MM)</span></div><div class='line' id='LC1125'><span class="sd">            3: ShowAndGetIPAddress (default format: #.#.#.#)</span></div><div class='line' id='LC1126'><br/></div><div class='line' id='LC1127'><span class="sd">        Note:</span></div><div class='line' id='LC1128'><span class="sd">            Returns the entered data as a string.</span></div><div class='line' id='LC1129'><span class="sd">            Returns the default value if dialog was canceled.</span></div><div class='line' id='LC1130'><br/></div><div class='line' id='LC1131'><span class="sd">        Example:</span></div><div class='line' id='LC1132'><span class="sd">            dialog = xbmcgui.Dialog()</span></div><div class='line' id='LC1133'><span class="sd">            d = dialog.numeric(1, &#39;Enter date of birth&#39;)</span></div><div class='line' id='LC1134'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC1135'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC1136'><br/></div><div class='line' id='LC1137'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">yesno</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">heading</span><span class="p">,</span> <span class="n">line1</span><span class="p">,</span> <span class="n">line2</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">line3</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">nolabel</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">yeslabel</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC1138'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Show a dialog &#39;YES/NO&#39;.</span></div><div class='line' id='LC1139'><br/></div><div class='line' id='LC1140'><span class="sd">        heading: string or unicode - dialog heading.</span></div><div class='line' id='LC1141'><span class="sd">        line1: string or unicode - line #1 text.</span></div><div class='line' id='LC1142'><span class="sd">        line2: string or unicode - line #2 text.</span></div><div class='line' id='LC1143'><span class="sd">        line3: string or unicode - line #3 text.</span></div><div class='line' id='LC1144'><span class="sd">        nolabel: label to put on the no button.</span></div><div class='line' id='LC1145'><span class="sd">        yeslabel: label to put on the yes button.</span></div><div class='line' id='LC1146'><br/></div><div class='line' id='LC1147'><span class="sd">        Note:</span></div><div class='line' id='LC1148'><span class="sd">            Returns True if &#39;Yes&#39; was pressed, else False.</span></div><div class='line' id='LC1149'><br/></div><div class='line' id='LC1150'><span class="sd">        Example:</span></div><div class='line' id='LC1151'><span class="sd">            dialog = xbmcgui.Dialog()</span></div><div class='line' id='LC1152'><span class="sd">            ret = dialog.yesno(&#39;XBMC&#39;, &#39;Do you want to exit this script?&#39;)</span></div><div class='line' id='LC1153'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC1154'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">bool</span></div><div class='line' id='LC1155'><br/></div><div class='line' id='LC1156'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">select</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">heading</span><span class="p">,</span> <span class="nb">list</span><span class="p">,</span> <span class="n">autoclose</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span></div><div class='line' id='LC1157'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Show a select dialog.</span></div><div class='line' id='LC1158'><br/></div><div class='line' id='LC1159'><span class="sd">        heading: string or unicode - dialog heading.</span></div><div class='line' id='LC1160'><span class="sd">        list: string list - list of items.</span></div><div class='line' id='LC1161'><span class="sd">        autoclose: integer - milliseconds to autoclose dialog.</span></div><div class='line' id='LC1162'><br/></div><div class='line' id='LC1163'><span class="sd">        Note:</span></div><div class='line' id='LC1164'><span class="sd">            autoclose = 0 - This disables autoclose.</span></div><div class='line' id='LC1165'><span class="sd">            Returns the position of the highlighted item as an integer.</span></div><div class='line' id='LC1166'><br/></div><div class='line' id='LC1167'><span class="sd">        Example:</span></div><div class='line' id='LC1168'><span class="sd">            dialog = xbmcgui.Dialog()</span></div><div class='line' id='LC1169'><span class="sd">            ret = dialog.select(&#39;Choose a playlist&#39;, [&#39;Playlist #1&#39;, &#39;Playlist #2, &#39;Playlist #3&#39;])</span></div><div class='line' id='LC1170'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC1171'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">int</span></div><div class='line' id='LC1172'><br/></div><div class='line' id='LC1173'><br/></div><div class='line' id='LC1174'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC1175'><span class="k">class</span> <span class="nc">DialogProgress</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC1176'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">create</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">heading</span><span class="p">,</span> <span class="n">line1</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">line2</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">line3</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC1177'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Create and show a progress dialog.</span></div><div class='line' id='LC1178'><br/></div><div class='line' id='LC1179'><span class="sd">        heading: string or unicode - dialog heading.</span></div><div class='line' id='LC1180'><span class="sd">        line1: string or unicode - line #1 text.</span></div><div class='line' id='LC1181'><span class="sd">        line2: string or unicode - line #2 text.</span></div><div class='line' id='LC1182'><span class="sd">        line3: string or unicode - line #3 text.</span></div><div class='line' id='LC1183'><br/></div><div class='line' id='LC1184'><span class="sd">        Note:</span></div><div class='line' id='LC1185'><span class="sd">            Use update() to update lines and progressbar.</span></div><div class='line' id='LC1186'><br/></div><div class='line' id='LC1187'><span class="sd">        Example:</span></div><div class='line' id='LC1188'><span class="sd">            pDialog = xbmcgui.DialogProgress()</span></div><div class='line' id='LC1189'><span class="sd">            ret = pDialog.create(&#39;XBMC&#39;, &#39;Initializing script...&#39;)</span></div><div class='line' id='LC1190'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC1191'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC1192'><br/></div><div class='line' id='LC1193'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">update</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">percent</span><span class="p">,</span> <span class="n">line1</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">line2</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">line3</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC1194'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Update&#39;s the progress dialog.</span></div><div class='line' id='LC1195'><br/></div><div class='line' id='LC1196'><span class="sd">        percent: integer - percent complete. (0:100)</span></div><div class='line' id='LC1197'><span class="sd">        line1: string or unicode - line #1 text.</span></div><div class='line' id='LC1198'><span class="sd">        line2: string or unicode - line #2 text.</span></div><div class='line' id='LC1199'><span class="sd">        line3: string or unicode - line #3 text.</span></div><div class='line' id='LC1200'><br/></div><div class='line' id='LC1201'><span class="sd">        Note:</span></div><div class='line' id='LC1202'><span class="sd">            If percent == 0, the progressbar will be hidden.</span></div><div class='line' id='LC1203'><br/></div><div class='line' id='LC1204'><span class="sd">        Example:</span></div><div class='line' id='LC1205'><span class="sd">            pDialog.update(25, &#39;Importing modules...&#39;)</span></div><div class='line' id='LC1206'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC1207'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC1208'><br/></div><div class='line' id='LC1209'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">iscanceled</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC1210'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns True if the user pressed cancel.&quot;&quot;&quot;</span></div><div class='line' id='LC1211'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">bool</span></div><div class='line' id='LC1212'><br/></div><div class='line' id='LC1213'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">close</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC1214'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Close the progress dialog.&quot;&quot;&quot;</span></div><div class='line' id='LC1215'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC1216'><br/></div><div class='line' id='LC1217'><br/></div><div class='line' id='LC1218'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC1219'><span class="k">class</span> <span class="nc">Action</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC1220'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Action class.</span></div><div class='line' id='LC1221'><br/></div><div class='line' id='LC1222'><span class="sd">    For backwards compatibility reasons the == operator is extended so that it</span></div><div class='line' id='LC1223'><span class="sd">    can compare an action with other actions and action.GetID() with numbers.</span></div><div class='line' id='LC1224'><br/></div><div class='line' id='LC1225'><span class="sd">    Example:</span></div><div class='line' id='LC1226'><span class="sd">        (action == ACTION_MOVE_LEFT)</span></div><div class='line' id='LC1227'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC1228'><br/></div><div class='line' id='LC1229'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getId</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC1230'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the action&#39;s current id as a long or 0 if no action is mapped in the xml&#39;s.&quot;&quot;&quot;</span></div><div class='line' id='LC1231'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">long</span></div><div class='line' id='LC1232'><br/></div><div class='line' id='LC1233'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getButtonCode</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC1234'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the button code for this action.&quot;&quot;&quot;</span></div><div class='line' id='LC1235'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">long</span></div><div class='line' id='LC1236'><br/></div><div class='line' id='LC1237'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getAmount1</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC1238'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the first amount of force applied to the thumbstick.&quot;&quot;&quot;</span></div><div class='line' id='LC1239'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">float</span></div><div class='line' id='LC1240'><br/></div><div class='line' id='LC1241'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getAmount2</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC1242'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the second amount of force applied to the thumbstick.&quot;&quot;&quot;</span></div><div class='line' id='LC1243'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">float</span></div><div class='line' id='LC1244'><br/></div><div class='line' id='LC1245'><br/></div><div class='line' id='LC1246'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC1247'><span class="k">class</span> <span class="nc">ControlRadioButton</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC1248'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">width</span><span class="p">,</span> <span class="n">height</span><span class="p">,</span> <span class="n">label</span><span class="p">,</span> <span class="n">focusTexture</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">noFocusTexture</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">textOffsetX</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></div><div class='line' id='LC1249'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">textOffsetY</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">alignment</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">font</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">textColor</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">disabledColor</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">angle</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></div><div class='line' id='LC1250'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">shadowColor</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">focusedColor</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">radiuFocusTexture</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">noRadioFocusTexture</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC1251'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;ControlRadioButton class.</span></div><div class='line' id='LC1252'><br/></div><div class='line' id='LC1253'><span class="sd">        x: integer - x coordinate of control.</span></div><div class='line' id='LC1254'><span class="sd">        y: integer - y coordinate of control.</span></div><div class='line' id='LC1255'><span class="sd">        width: integer - width of control.</span></div><div class='line' id='LC1256'><span class="sd">        height: integer - height of control.</span></div><div class='line' id='LC1257'><span class="sd">        label: string or unicode - text string.</span></div><div class='line' id='LC1258'><span class="sd">        focusTexture: string - filename for focus texture.</span></div><div class='line' id='LC1259'><span class="sd">        noFocusTexture: string - filename for no focus texture.</span></div><div class='line' id='LC1260'><span class="sd">        textOffsetX: integer - x offset of label.</span></div><div class='line' id='LC1261'><span class="sd">        textOffsetY: integer - y offset of label.</span></div><div class='line' id='LC1262'><span class="sd">        alignment: integer - alignment of label - *Note, see xbfont.h</span></div><div class='line' id='LC1263'><span class="sd">        font: string - font used for label text. (e.g. &#39;font13&#39;)</span></div><div class='line' id='LC1264'><span class="sd">        textColor: hexstring - color of enabled radio button&#39;s label. (e.g. &#39;0xFFFFFFFF&#39;)</span></div><div class='line' id='LC1265'><span class="sd">        disabledColor: hexstring - color of disabled radio button&#39;s label. (e.g. &#39;0xFFFF3300&#39;)</span></div><div class='line' id='LC1266'><span class="sd">        angle: integer - angle of control. (+ rotates CCW, - rotates CW)</span></div><div class='line' id='LC1267'><span class="sd">        shadowColor: hexstring - color of radio button&#39;s label&#39;s shadow. (e.g. &#39;0xFF000000&#39;)</span></div><div class='line' id='LC1268'><span class="sd">        focusedColor: hexstring - color of focused radio button&#39;s label. (e.g. &#39;0xFF00FFFF&#39;)</span></div><div class='line' id='LC1269'><span class="sd">        radioFocusTexture: string - filename for radio focus texture.</span></div><div class='line' id='LC1270'><span class="sd">        noRadioFocusTexture: string - filename for radio no focus texture.</span></div><div class='line' id='LC1271'><br/></div><div class='line' id='LC1272'><span class="sd">        Note:</span></div><div class='line' id='LC1273'><span class="sd">            After you create the control, you need to add it to the window with addControl().</span></div><div class='line' id='LC1274'><br/></div><div class='line' id='LC1275'><span class="sd">        Example:</span></div><div class='line' id='LC1276'><span class="sd">            self.radiobutton = xbmcgui.ControlRadioButton(100, 250, 200, 50, &#39;Status&#39;, font=&#39;font14&#39;)</span></div><div class='line' id='LC1277'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC1278'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC1279'><br/></div><div class='line' id='LC1280'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setSelected</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">selected</span><span class="p">):</span></div><div class='line' id='LC1281'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Sets the radio buttons&#39;s selected status.</span></div><div class='line' id='LC1282'><br/></div><div class='line' id='LC1283'><span class="sd">        selected: bool - True=selected (on) / False=not selected (off)</span></div><div class='line' id='LC1284'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC1285'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC1286'><br/></div><div class='line' id='LC1287'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">isSelected</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC1288'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the radio buttons&#39;s selected status.&quot;&quot;&quot;</span></div><div class='line' id='LC1289'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">bool</span></div><div class='line' id='LC1290'><br/></div><div class='line' id='LC1291'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setLabel</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">label</span><span class="p">,</span> <span class="n">font</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">textColor</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">disabledColor</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">shadowColor</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">focusedColor</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC1292'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Set&#39;s the radio buttons text attributes.</span></div><div class='line' id='LC1293'><br/></div><div class='line' id='LC1294'><span class="sd">        label: string or unicode - text string.</span></div><div class='line' id='LC1295'><span class="sd">        font: string - font used for label text. (e.g. &#39;font13&#39;)</span></div><div class='line' id='LC1296'><span class="sd">        textColor: hexstring - color of enabled radio button&#39;s label. (e.g. &#39;0xFFFFFFFF&#39;)</span></div><div class='line' id='LC1297'><span class="sd">        disabledColor: hexstring - color of disabled radio button&#39;s label. (e.g. &#39;0xFFFF3300&#39;)</span></div><div class='line' id='LC1298'><span class="sd">        shadowColor: hexstring - color of radio button&#39;s label&#39;s shadow. (e.g. &#39;0xFF000000&#39;)</span></div><div class='line' id='LC1299'><span class="sd">        focusedColor: hexstring - color of focused radio button&#39;s label. (e.g. &#39;0xFFFFFF00&#39;)</span></div><div class='line' id='LC1300'><br/></div><div class='line' id='LC1301'><span class="sd">        Example:</span></div><div class='line' id='LC1302'><span class="sd">            self.radiobutton.setLabel(&#39;Status&#39;, &#39;font14&#39;, &#39;0xFFFFFFFF&#39;, &#39;0xFFFF3300&#39;, &#39;0xFF000000&#39;)</span></div><div class='line' id='LC1303'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC1304'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC1305'><br/></div><div class='line' id='LC1306'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setRadioDimension</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">width</span><span class="p">,</span> <span class="n">height</span><span class="p">):</span></div><div class='line' id='LC1307'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Sets the radio buttons&#39;s radio texture&#39;s position and size.</span></div><div class='line' id='LC1308'><br/></div><div class='line' id='LC1309'><span class="sd">        x: integer - x coordinate of radio texture.</span></div><div class='line' id='LC1310'><span class="sd">        y: integer - y coordinate of radio texture.</span></div><div class='line' id='LC1311'><span class="sd">        width: integer - width of radio texture.</span></div><div class='line' id='LC1312'><span class="sd">        height: integer - height of radio texture.</span></div><div class='line' id='LC1313'><br/></div><div class='line' id='LC1314'><span class="sd">        Example:</span></div><div class='line' id='LC1315'><span class="sd">            self.radiobutton.setRadioDimension(x=100, y=5, width=20, height=20)</span></div><div class='line' id='LC1316'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC1317'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC1318'><br/></div><div class='line' id='LC1319'><br/></div><div class='line' id='LC1320'><span class="n">ICON_OVERLAY_NONE</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC1321'><span class="n">ICON_OVERLAY_RAR</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC1322'><span class="n">ICON_OVERLAY_ZIP</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC1323'><span class="n">ICON_OVERLAY_LOCKED</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC1324'><span class="n">ICON_OVERLAY_HAS_TRAINER</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC1325'><span class="n">ICON_OVERLAY_TRAINED</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC1326'><span class="n">ICON_OVERLAY_UNWATCHED</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC1327'><span class="n">ICON_OVERLAY_WATCHED</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC1328'><span class="n">ICON_OVERLAY_HD</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC1329'><br/></div><div class='line' id='LC1330'><span class="k">def</span> <span class="nf">lock</span><span class="p">():</span></div><div class='line' id='LC1331'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Lock the gui until xbmcgui.unlock() is called.</span></div><div class='line' id='LC1332'><br/></div><div class='line' id='LC1333'><span class="sd">    Note:</span></div><div class='line' id='LC1334'><span class="sd">        This will improve performance when doing a lot of gui manipulation at once.</span></div><div class='line' id='LC1335'><span class="sd">        The main program (xbmc itself) will freeze until xbmcgui.unlock() is called.</span></div><div class='line' id='LC1336'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC1337'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC1338'><br/></div><div class='line' id='LC1339'><span class="k">def</span> <span class="nf">unlock</span><span class="p">():</span></div><div class='line' id='LC1340'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Unlock the gui from a lock() call.&quot;&quot;&quot;</span></div><div class='line' id='LC1341'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC1342'><br/></div><div class='line' id='LC1343'><span class="k">def</span> <span class="nf">getCurrentWindowId</span><span class="p">():</span></div><div class='line' id='LC1344'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the id for the current &#39;active&#39; window as an integer.&quot;&quot;&quot;</span></div><div class='line' id='LC1345'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">long</span></div><div class='line' id='LC1346'><br/></div><div class='line' id='LC1347'><span class="k">def</span> <span class="nf">getCurrentWindowDialogId</span><span class="p">():</span></div><div class='line' id='LC1348'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the id for the current &#39;active&#39; dialog as an integer.&quot;&quot;&quot;</span></div><div class='line' id='LC1349'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">long</span></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2013 <span title="0.05399s from fe3.rs.github.com">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/Tenzer/xbmcstubs/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-remove-close close ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>

    
  </body>
</html>

