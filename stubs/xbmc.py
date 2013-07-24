


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>xbmcstubs/xbmc.py at master · Tenzer/xbmcstubs · GitHub</title>
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

        <link data-pjax-transient rel='permalink' href='/Tenzer/xbmcstubs/blob/be31664f64468bf4d03bdcc2a521aa0418591094/xbmc.py'>
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
      <a class="button" href="/login?return_to=%2FTenzer%2Fxbmcstubs%2Fblob%2Fmaster%2Fxbmc.py">Sign in</a>
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
          


<!-- blob contrib key: blob_contributors:v21:a6680d2c07fe2af7245c72ae60fd336a -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:a6680d2c07fe2af7245c72ae60fd336a -->

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
              <a href="/Tenzer/xbmcstubs/blob/Dharma/xbmc.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="Dharma" data-skip-pjax="true" rel="nofollow" title="Dharma">Dharma</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Tenzer/xbmcstubs/blob/master/xbmc.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" data-skip-pjax="true" rel="nofollow" title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Tenzer/xbmcstubs/blob/Dharma.01/xbmc.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="Dharma.01" data-skip-pjax="true" rel="nofollow" title="Dharma.01">Dharma.01</a>
            </div> <!-- /.select-menu-item -->
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/Tenzer/xbmcstubs" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">xbmcstubs</span></a></span></span><span class="separator"> / </span><strong class="final-path">xbmc.py</strong> <span class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="xbmc.py" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
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
          <a class="avatar tooltipped downwards" title="Tenzer" href="/Tenzer/xbmcstubs/commits/master/xbmc.py?author=Tenzer"><img height="20" src="https://secure.gravatar.com/avatar/6a6fdd7ce2437edf3c0f2889dbcaafc5?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="twinther" href="/Tenzer/xbmcstubs/commits/master/xbmc.py?author=twinther"><img height="20" src="https://secure.gravatar.com/avatar/3e99ac637d6f97b5f129118aef8b92c7?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>


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
          <span>859 lines (634 sloc)</span>
        <span>21.646 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
              <a class="minibutton js-entice" href=""
                 data-entice="You must be signed in to make or propose changes">Edit</a>
          <a href="/Tenzer/xbmcstubs/raw/master/xbmc.py" class="button minibutton " id="raw-url">Raw</a>
            <a href="/Tenzer/xbmcstubs/blame/master/xbmc.py" class="button minibutton ">Blame</a>
          <a href="/Tenzer/xbmcstubs/commits/master/xbmc.py" class="button minibutton " rel="nofollow">History</a>
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

          </td>
          <td class="blob-line-code">
                  <div class="highlight"><pre><div class='line' id='LC1'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC2'><span class="k">class</span> <span class="nc">Keyboard</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC3'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">heading</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">hidden</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span></div><div class='line' id='LC4'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Creates a new Keyboard object with default text heading and hidden input flag if supplied.</span></div><div class='line' id='LC5'><br/></div><div class='line' id='LC6'><span class="sd">        default: string - default text entry.</span></div><div class='line' id='LC7'><span class="sd">        heading: string - keyboard heading.</span></div><div class='line' id='LC8'><span class="sd">        hidden: boolean - True for hidden text entry.</span></div><div class='line' id='LC9'><br/></div><div class='line' id='LC10'><span class="sd">        Example:</span></div><div class='line' id='LC11'><span class="sd">            kb = xbmc.Keyboard(&#39;default&#39;, &#39;heading&#39;, True)</span></div><div class='line' id='LC12'><span class="sd">            kb.setDefault(&#39;password&#39;) # optional</span></div><div class='line' id='LC13'><span class="sd">            kb.setHeading(&#39;Enter password&#39;) # optional</span></div><div class='line' id='LC14'><span class="sd">            kb.setHiddenInput(True) # optional</span></div><div class='line' id='LC15'><span class="sd">            kb.doModal()</span></div><div class='line' id='LC16'><span class="sd">            if (kb.isConfirmed()):</span></div><div class='line' id='LC17'><span class="sd">                text = kb.getText()</span></div><div class='line' id='LC18'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC19'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC20'><br/></div><div class='line' id='LC21'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">doModal</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">autoclose</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span></div><div class='line' id='LC22'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Show keyboard and wait for user action.</span></div><div class='line' id='LC23'><br/></div><div class='line' id='LC24'><span class="sd">        autoclose: integer - milliseconds to autoclose dialog.</span></div><div class='line' id='LC25'><br/></div><div class='line' id='LC26'><span class="sd">        Note:</span></div><div class='line' id='LC27'><span class="sd">            autoclose = 0 - This disables autoclose</span></div><div class='line' id='LC28'><br/></div><div class='line' id='LC29'><span class="sd">        Example:</span></div><div class='line' id='LC30'><span class="sd">            kb.doModal(30000)</span></div><div class='line' id='LC31'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC32'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC33'><br/></div><div class='line' id='LC34'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setDefault</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">default</span><span class="p">):</span></div><div class='line' id='LC35'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Set the default text entry.</span></div><div class='line' id='LC36'><br/></div><div class='line' id='LC37'><span class="sd">        default: string - default text entry.</span></div><div class='line' id='LC38'><br/></div><div class='line' id='LC39'><span class="sd">        Example:</span></div><div class='line' id='LC40'><span class="sd">            kb.setDefault(&#39;password&#39;)</span></div><div class='line' id='LC41'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC42'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC43'><br/></div><div class='line' id='LC44'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setHiddenInput</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">hidden</span><span class="p">):</span></div><div class='line' id='LC45'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Allows hidden text entry.</span></div><div class='line' id='LC46'><br/></div><div class='line' id='LC47'><span class="sd">        hidden: boolean - True for hidden text entry.</span></div><div class='line' id='LC48'><br/></div><div class='line' id='LC49'><span class="sd">        Example:</span></div><div class='line' id='LC50'><span class="sd">            kb.setHiddenInput(True)</span></div><div class='line' id='LC51'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC52'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC53'><br/></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setHeading</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">heading</span><span class="p">):</span></div><div class='line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Set the keyboard heading.</span></div><div class='line' id='LC56'><br/></div><div class='line' id='LC57'><span class="sd">        heading: string - keyboard heading.</span></div><div class='line' id='LC58'><br/></div><div class='line' id='LC59'><span class="sd">        Example:</span></div><div class='line' id='LC60'><span class="sd">            kb.setHeading(&#39;Enter password&#39;)</span></div><div class='line' id='LC61'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC63'><br/></div><div class='line' id='LC64'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getText</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the user input as a string.</span></div><div class='line' id='LC66'><br/></div><div class='line' id='LC67'><span class="sd">        Note:</span></div><div class='line' id='LC68'><span class="sd">            This will always return the text entry even if you cancel the keyboard.</span></div><div class='line' id='LC69'><span class="sd">            Use the isConfirmed() method to check if user cancelled the keyboard.</span></div><div class='line' id='LC70'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC72'><br/></div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">isConfirmed</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC74'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns False if the user cancelled the input.&quot;&quot;&quot;</span></div><div class='line' id='LC75'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">bool</span></div><div class='line' id='LC76'><br/></div><div class='line' id='LC77'><br/></div><div class='line' id='LC78'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC79'><span class="k">class</span> <span class="nc">Player</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC80'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">core</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC81'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Creates a new Player with as default the xbmc music playlist.</span></div><div class='line' id='LC82'><br/></div><div class='line' id='LC83'><span class="sd">        Args:</span></div><div class='line' id='LC84'><span class="sd">            core: Use a specified playcore instead of letting xbmc decide the playercore to use.</span></div><div class='line' id='LC85'><span class="sd">                - xbmc.PLAYER_CORE_AUTO</span></div><div class='line' id='LC86'><span class="sd">                - xbmc.PLAYER_CORE_DVDPLAYER</span></div><div class='line' id='LC87'><span class="sd">                - xbmc.PLAYER_CORE_MPLAYER</span></div><div class='line' id='LC88'><span class="sd">                - xbmc.PLAYER_CORE_PAPLAYER</span></div><div class='line' id='LC89'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC90'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC91'><br/></div><div class='line' id='LC92'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">play</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">listitem</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">windowed</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span></div><div class='line' id='LC93'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Play this item.</span></div><div class='line' id='LC94'><br/></div><div class='line' id='LC95'><span class="sd">        item: string - filename, url or playlist.</span></div><div class='line' id='LC96'><span class="sd">        listitem: listitem - used with setInfo() to set different infolabels.</span></div><div class='line' id='LC97'><span class="sd">        windowed: bool - True=play video windowed, False=play users preference.</span></div><div class='line' id='LC98'><br/></div><div class='line' id='LC99'><span class="sd">        Note:</span></div><div class='line' id='LC100'><span class="sd">            If item is not given then the player will try to play the current item in the current playlist.</span></div><div class='line' id='LC101'><br/></div><div class='line' id='LC102'><span class="sd">        Example:</span></div><div class='line' id='LC103'><span class="sd">            listitem = xbmcgui.ListItem(&#39;Ironman&#39;)</span></div><div class='line' id='LC104'><span class="sd">            listitem.setInfo(&#39;video&#39;, {&#39;Title&#39;: &#39;Ironman&#39;, &#39;Genre&#39;: &#39;Science Fiction&#39;})</span></div><div class='line' id='LC105'><span class="sd">            xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(url, listitem, windowed)</span></div><div class='line' id='LC106'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC107'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC108'><br/></div><div class='line' id='LC109'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC110'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Stop playing.&quot;&quot;&quot;</span></div><div class='line' id='LC111'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC112'><br/></div><div class='line' id='LC113'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">pause</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC114'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Pause playing.&quot;&quot;&quot;</span></div><div class='line' id='LC115'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC116'><br/></div><div class='line' id='LC117'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">playnext</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Play next item in playlist.&quot;&quot;&quot;</span></div><div class='line' id='LC119'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC120'><br/></div><div class='line' id='LC121'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">playprevious</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC122'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Play previous item in playlist.&quot;&quot;&quot;</span></div><div class='line' id='LC123'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC124'><br/></div><div class='line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">playselected</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC126'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Play a certain item from the current playlist.&quot;&quot;&quot;</span></div><div class='line' id='LC127'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC128'><br/></div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">onPlayBackStarted</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC130'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Will be called when xbmc starts playing a file.&quot;&quot;&quot;</span></div><div class='line' id='LC131'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC132'><br/></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">onPlayBackEnded</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC134'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Will be called when xbmc stops playing a file.&quot;&quot;&quot;</span></div><div class='line' id='LC135'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC136'><br/></div><div class='line' id='LC137'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">onPlayBackStopped</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC138'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Will be called when user stops xbmc playing a file.&quot;&quot;&quot;</span></div><div class='line' id='LC139'><br/></div><div class='line' id='LC140'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">onPlayBackPaused</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC141'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Will be called when user pauses a playing file.&quot;&quot;&quot;</span></div><div class='line' id='LC142'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC143'><br/></div><div class='line' id='LC144'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">onPlayBackResumed</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Will be called when user resumes a paused file.&quot;&quot;&quot;</span></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC147'><br/></div><div class='line' id='LC148'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">isPlaying</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC149'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns True is xbmc is playing a file.&quot;&quot;&quot;</span></div><div class='line' id='LC150'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">bool</span></div><div class='line' id='LC151'><br/></div><div class='line' id='LC152'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">isPlayingAudio</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC153'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns True is xbmc is playing an audio file.&quot;&quot;&quot;</span></div><div class='line' id='LC154'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">bool</span></div><div class='line' id='LC155'><br/></div><div class='line' id='LC156'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">isPlayingVideo</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC157'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns True if xbmc is playing a video.&quot;&quot;&quot;</span></div><div class='line' id='LC158'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">bool</span></div><div class='line' id='LC159'><br/></div><div class='line' id='LC160'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getPlayingFile</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC161'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the current playing file as a string.</span></div><div class='line' id='LC162'><br/></div><div class='line' id='LC163'><span class="sd">        Raises:</span></div><div class='line' id='LC164'><span class="sd">            Exception: If player is not playing a file.</span></div><div class='line' id='LC165'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC166'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC167'><br/></div><div class='line' id='LC168'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getVideoInfoTag</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC169'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the VideoInfoTag of the current playing Movie.</span></div><div class='line' id='LC170'><br/></div><div class='line' id='LC171'><span class="sd">        Raises:</span></div><div class='line' id='LC172'><span class="sd">            Exception: If player is not playing a file or current file is not a movie file.</span></div><div class='line' id='LC173'><br/></div><div class='line' id='LC174'><span class="sd">        Note:</span></div><div class='line' id='LC175'><span class="sd">            This doesn&#39;t work yet, it&#39;s not tested.</span></div><div class='line' id='LC176'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC177'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">object</span></div><div class='line' id='LC178'><br/></div><div class='line' id='LC179'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getMusicInfoTag</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC180'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the MusicInfoTag of the current playing &#39;Song&#39;.</span></div><div class='line' id='LC181'><br/></div><div class='line' id='LC182'><span class="sd">        Raises:</span></div><div class='line' id='LC183'><span class="sd">            Exception: If player is not playing a file or current file is not a music file.</span></div><div class='line' id='LC184'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC185'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">object</span></div><div class='line' id='LC186'><br/></div><div class='line' id='LC187'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getTotalTime</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC188'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the total time of the current playing media in seconds.</span></div><div class='line' id='LC189'><br/></div><div class='line' id='LC190'><span class="sd">        This is only accurate to the full second.</span></div><div class='line' id='LC191'><br/></div><div class='line' id='LC192'><span class="sd">        Raises:</span></div><div class='line' id='LC193'><span class="sd">            Exception: If player is not playing a file.</span></div><div class='line' id='LC194'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC195'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">float</span></div><div class='line' id='LC196'><br/></div><div class='line' id='LC197'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getTime</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC198'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the current time of the current playing media as fractional seconds.</span></div><div class='line' id='LC199'><br/></div><div class='line' id='LC200'><span class="sd">        Raises:</span></div><div class='line' id='LC201'><span class="sd">            Exception: If player is not playing a file.</span></div><div class='line' id='LC202'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC203'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">float</span></div><div class='line' id='LC204'><br/></div><div class='line' id='LC205'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">seekTime</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">pTime</span><span class="p">):</span></div><div class='line' id='LC206'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Seeks the specified amount of time as fractional seconds.</span></div><div class='line' id='LC207'><br/></div><div class='line' id='LC208'><span class="sd">        The time specified is relative to the beginning of the currently playing media file.</span></div><div class='line' id='LC209'><br/></div><div class='line' id='LC210'><span class="sd">        Raises:</span></div><div class='line' id='LC211'><span class="sd">            Exception: If player is not playing a file.</span></div><div class='line' id='LC212'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC213'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC214'><br/></div><div class='line' id='LC215'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setSubtitles</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC216'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Set subtitle file and enable subtitles.</span></div><div class='line' id='LC217'><br/></div><div class='line' id='LC218'><span class="sd">        path: string or unicode - Path to subtitle.</span></div><div class='line' id='LC219'><br/></div><div class='line' id='LC220'><span class="sd">        Example:</span></div><div class='line' id='LC221'><span class="sd">            setSubtitles(&#39;/path/to/subtitle/test.srt&#39;)</span></div><div class='line' id='LC222'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC223'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC224'><br/></div><div class='line' id='LC225'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getSubtitles</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC226'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Get subtitle stream name.&quot;&quot;&quot;</span></div><div class='line' id='LC227'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC228'><br/></div><div class='line' id='LC229'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">disableSubtitles</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC230'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Disable subtitles.&quot;&quot;&quot;</span></div><div class='line' id='LC231'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC232'><br/></div><div class='line' id='LC233'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getAvailableAudioStreams</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC234'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Get audio stream names.&quot;&quot;&quot;</span></div><div class='line' id='LC235'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">list</span></div><div class='line' id='LC236'><br/></div><div class='line' id='LC237'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setAudioStream</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stream</span><span class="p">):</span></div><div class='line' id='LC238'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Set audio stream.</span></div><div class='line' id='LC239'><br/></div><div class='line' id='LC240'><span class="sd">        stream: int</span></div><div class='line' id='LC241'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC242'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC243'><br/></div><div class='line' id='LC244'><br/></div><div class='line' id='LC245'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC246'><span class="k">class</span> <span class="nc">PlayList</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC247'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">playlist</span><span class="p">):</span></div><div class='line' id='LC248'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Retrieve a reference from a valid xbmc playlist</span></div><div class='line' id='LC249'><br/></div><div class='line' id='LC250'><span class="sd">        playlist: int - can be one of the next values:</span></div><div class='line' id='LC251'><span class="sd">            0: xbmc.PLAYLIST_MUSIC</span></div><div class='line' id='LC252'><span class="sd">            1: xbmc.PLAYLIST_VIDEO</span></div><div class='line' id='LC253'><br/></div><div class='line' id='LC254'><span class="sd">        Use PlayList[int position] or __getitem__(int position) to get a PlayListItem.</span></div><div class='line' id='LC255'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC256'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC257'><br/></div><div class='line' id='LC258'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">,</span> <span class="n">listitem</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">index</span><span class="o">=-</span><span class="mi">1</span><span class="p">):</span></div><div class='line' id='LC259'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Adds a new file to the playlist.</span></div><div class='line' id='LC260'><br/></div><div class='line' id='LC261'><span class="sd">        url: string or unicode - filename or url to add.</span></div><div class='line' id='LC262'><span class="sd">        listitem: listitem - used with setInfo() to set different infolabels.</span></div><div class='line' id='LC263'><span class="sd">        index: integer - position to add playlist item.</span></div><div class='line' id='LC264'><br/></div><div class='line' id='LC265'><span class="sd">        Example:</span></div><div class='line' id='LC266'><span class="sd">            playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)</span></div><div class='line' id='LC267'><span class="sd">            video = &#39;F:\\movies\\Ironman.mov&#39;</span></div><div class='line' id='LC268'><span class="sd">            listitem = xbmcgui.ListItem(&#39;Ironman&#39;, thumbnailImage=&#39;F:\\movies\\Ironman.tbn&#39;)</span></div><div class='line' id='LC269'><span class="sd">            listitem.setInfo(&#39;video&#39;, {&#39;Title&#39;: &#39;Ironman&#39;, &#39;Genre&#39;: &#39;Science Fiction&#39;})</span></div><div class='line' id='LC270'><span class="sd">            playlist.add(url=video, listitem=listitem, index=7)</span></div><div class='line' id='LC271'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC272'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC273'><br/></div><div class='line' id='LC274'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">load</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">filename</span><span class="p">):</span></div><div class='line' id='LC275'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Load a playlist.</span></div><div class='line' id='LC276'><br/></div><div class='line' id='LC277'><span class="sd">        Clear current playlist and copy items from the file to this Playlist filename can be like .pls or .m3u ...</span></div><div class='line' id='LC278'><br/></div><div class='line' id='LC279'><span class="sd">        Returns False if unable to load playlist, True otherwise.</span></div><div class='line' id='LC280'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC281'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">bool</span></div><div class='line' id='LC282'><br/></div><div class='line' id='LC283'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">remove</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">filename</span><span class="p">):</span></div><div class='line' id='LC284'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Remove an item with this filename from the playlist.&quot;&quot;&quot;</span></div><div class='line' id='LC285'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC286'><br/></div><div class='line' id='LC287'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">clear</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC288'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Clear all items in the playlist.&quot;&quot;&quot;</span></div><div class='line' id='LC289'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC290'><br/></div><div class='line' id='LC291'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">shuffle</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC292'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Shuffle the playlist.&quot;&quot;&quot;</span></div><div class='line' id='LC293'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC294'><br/></div><div class='line' id='LC295'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">unshuffle</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC296'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Unshuffle the playlist.&quot;&quot;&quot;</span></div><div class='line' id='LC297'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC298'><br/></div><div class='line' id='LC299'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">size</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC300'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the total number of PlayListItems in this playlist.&quot;&quot;&quot;</span></div><div class='line' id='LC301'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">int</span></div><div class='line' id='LC302'><br/></div><div class='line' id='LC303'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getposition</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC304'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the position of the current song in this playlist.&quot;&quot;&quot;</span></div><div class='line' id='LC305'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">int</span></div><div class='line' id='LC306'><br/></div><div class='line' id='LC307'><br/></div><div class='line' id='LC308'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC309'><span class="k">class</span> <span class="nc">PlayListItem</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC310'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Creates a new PlaylistItem which can be added to a PlayList.&quot;&quot;&quot;</span></div><div class='line' id='LC311'><br/></div><div class='line' id='LC312'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getdescription</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC313'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the description of this PlayListItem.&quot;&quot;&quot;</span></div><div class='line' id='LC314'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC315'><br/></div><div class='line' id='LC316'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getduration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC317'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the duration of this PlayListItem.&quot;&quot;&quot;</span></div><div class='line' id='LC318'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">long</span></div><div class='line' id='LC319'><br/></div><div class='line' id='LC320'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getfilename</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC321'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the filename of this PlayListItem.&quot;&quot;&quot;</span></div><div class='line' id='LC322'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC323'><br/></div><div class='line' id='LC324'><br/></div><div class='line' id='LC325'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC326'><span class="k">class</span> <span class="nc">InfoTagMusic</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC327'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getURL</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC328'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC329'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC330'><br/></div><div class='line' id='LC331'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getTitle</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC332'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC333'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC334'><br/></div><div class='line' id='LC335'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getArtist</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC336'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC337'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC338'><br/></div><div class='line' id='LC339'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getAlbumArtist</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC340'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC341'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC342'><br/></div><div class='line' id='LC343'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getAlbum</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC344'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC345'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC346'><br/></div><div class='line' id='LC347'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getGenre</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC348'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC349'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC350'><br/></div><div class='line' id='LC351'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getDuration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC352'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns an integer.&quot;&quot;&quot;</span></div><div class='line' id='LC353'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">int</span></div><div class='line' id='LC354'><br/></div><div class='line' id='LC355'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getTrack</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC356'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns an integer.&quot;&quot;&quot;</span></div><div class='line' id='LC357'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">int</span></div><div class='line' id='LC358'><br/></div><div class='line' id='LC359'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getDisc</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC360'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns an integer.&quot;&quot;&quot;</span></div><div class='line' id='LC361'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">int</span></div><div class='line' id='LC362'><br/></div><div class='line' id='LC363'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getTrackAndDisc</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC364'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns an integer.&quot;&quot;&quot;</span></div><div class='line' id='LC365'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">int</span></div><div class='line' id='LC366'><br/></div><div class='line' id='LC367'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getReleaseDate</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC368'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC369'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC370'><br/></div><div class='line' id='LC371'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getListeners</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC372'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns an integer.&quot;&quot;&quot;</span></div><div class='line' id='LC373'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">int</span></div><div class='line' id='LC374'><br/></div><div class='line' id='LC375'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getPlayCount</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC376'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns an integer.&quot;&quot;&quot;</span></div><div class='line' id='LC377'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">int</span></div><div class='line' id='LC378'><br/></div><div class='line' id='LC379'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getLastPlayed</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC380'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC381'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC382'><br/></div><div class='line' id='LC383'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getComment</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC384'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC385'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC386'><br/></div><div class='line' id='LC387'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getLyrics</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC388'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC389'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC390'><br/></div><div class='line' id='LC391'><br/></div><div class='line' id='LC392'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC393'><span class="k">class</span> <span class="nc">InfoTagVideo</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC394'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getDirector</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC395'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC396'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC397'><br/></div><div class='line' id='LC398'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getWritingCredits</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC399'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC400'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC401'><br/></div><div class='line' id='LC402'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getGenre</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC403'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC404'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC405'><br/></div><div class='line' id='LC406'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getTagLine</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC407'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC408'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC409'><br/></div><div class='line' id='LC410'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getPlotOutline</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC411'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC412'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC413'><br/></div><div class='line' id='LC414'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getPlot</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC415'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC416'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC417'><br/></div><div class='line' id='LC418'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getPictureURL</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC419'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC420'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC421'><br/></div><div class='line' id='LC422'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getTitle</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC423'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC424'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC425'><br/></div><div class='line' id='LC426'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getOriginalTitle</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC427'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC428'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC429'><br/></div><div class='line' id='LC430'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getVotes</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC431'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC432'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC433'><br/></div><div class='line' id='LC434'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getCast</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC435'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC436'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC437'><br/></div><div class='line' id='LC438'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getFile</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC439'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC440'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC441'><br/></div><div class='line' id='LC442'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getPath</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC443'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC444'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC445'><br/></div><div class='line' id='LC446'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getIMDBNumber</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC447'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC448'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC449'><br/></div><div class='line' id='LC450'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getYear</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC451'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns an integer.&quot;&quot;&quot;</span></div><div class='line' id='LC452'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">int</span></div><div class='line' id='LC453'><br/></div><div class='line' id='LC454'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getPremiered</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC455'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC456'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC457'><br/></div><div class='line' id='LC458'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getFirstAired</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC459'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC460'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC461'><br/></div><div class='line' id='LC462'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getRating</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC463'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a float.&quot;&quot;&quot;</span></div><div class='line' id='LC464'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">float</span></div><div class='line' id='LC465'><br/></div><div class='line' id='LC466'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getPlayCount</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC467'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns an integer.&quot;&quot;&quot;</span></div><div class='line' id='LC468'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">int</span></div><div class='line' id='LC469'><br/></div><div class='line' id='LC470'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getLastPlayed</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC471'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a string.&quot;&quot;&quot;</span></div><div class='line' id='LC472'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC473'><br/></div><div class='line' id='LC474'><br/></div><div class='line' id='LC475'><span class="n">PLAYLIST_MUSIC</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC476'><span class="n">PLAYLIST_VIDEO</span> <span class="o">=</span> <span class="mi">1</span></div><div class='line' id='LC477'><br/></div><div class='line' id='LC478'><span class="n">PLAYER_CORE_AUTO</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC479'><span class="n">PLAYER_CORE_DVDPLAYER</span> <span class="o">=</span> <span class="mi">1</span></div><div class='line' id='LC480'><span class="n">PLAYER_CORE_MPLAYER</span> <span class="o">=</span> <span class="mi">2</span></div><div class='line' id='LC481'><span class="n">PLAYER_CORE_PAPLAYER</span> <span class="o">=</span> <span class="mi">3</span></div><div class='line' id='LC482'><br/></div><div class='line' id='LC483'><span class="n">TRAY_OPEN</span> <span class="o">=</span> <span class="mi">16</span></div><div class='line' id='LC484'><span class="n">DRIVE_NOT_READY</span> <span class="o">=</span> <span class="mi">1</span></div><div class='line' id='LC485'><span class="n">TRAY_CLOSED_NO_MEDIA</span> <span class="o">=</span> <span class="mi">64</span></div><div class='line' id='LC486'><span class="n">TRAY_CLOSED_MEDIA_PRESENT</span> <span class="o">=</span> <span class="mi">96</span></div><div class='line' id='LC487'><br/></div><div class='line' id='LC488'><span class="n">LOGDEBUG</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC489'><span class="n">LOGINFO</span> <span class="o">=</span> <span class="mi">1</span></div><div class='line' id='LC490'><span class="n">LOGNOTICE</span> <span class="o">=</span> <span class="mi">2</span></div><div class='line' id='LC491'><span class="n">LOGWARNING</span> <span class="o">=</span> <span class="mi">3</span></div><div class='line' id='LC492'><span class="n">LOGERROR</span> <span class="o">=</span> <span class="mi">4</span></div><div class='line' id='LC493'><span class="n">LOGSEVERE</span> <span class="o">=</span> <span class="mi">5</span></div><div class='line' id='LC494'><span class="n">LOGFATAL</span> <span class="o">=</span> <span class="mi">6</span></div><div class='line' id='LC495'><span class="n">LOGNONE</span> <span class="o">=</span> <span class="mi">7</span></div><div class='line' id='LC496'><br/></div><div class='line' id='LC497'><span class="n">CAPTURE_STATE_WORKING</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC498'><span class="n">CAPTURE_STATE_DONE</span> <span class="o">=</span> <span class="mi">3</span></div><div class='line' id='LC499'><span class="n">CAPTURE_STATE_FAILED</span> <span class="o">=</span> <span class="mi">4</span></div><div class='line' id='LC500'><br/></div><div class='line' id='LC501'><span class="n">CAPTURE_FLAG_CONTINUOUS</span> <span class="o">=</span> <span class="mi">1</span></div><div class='line' id='LC502'><span class="n">CAPTURE_FLAG_IMMEDIATELY</span> <span class="o">=</span> <span class="mi">2</span></div><div class='line' id='LC503'><br/></div><div class='line' id='LC504'><br/></div><div class='line' id='LC505'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC506'><span class="k">def</span> <span class="nf">output</span><span class="p">(</span><span class="n">msg</span><span class="p">,</span> <span class="n">level</span><span class="o">=</span><span class="n">LOGNOTICE</span><span class="p">):</span></div><div class='line' id='LC507'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Write a string to XBMC&#39;s log file and the debug window.</span></div><div class='line' id='LC508'><br/></div><div class='line' id='LC509'><span class="sd">    msg: string - text to output.</span></div><div class='line' id='LC510'><span class="sd">    level: integer - log level to ouput at.</span></div><div class='line' id='LC511'><br/></div><div class='line' id='LC512'><span class="sd">    Note:</span></div><div class='line' id='LC513'><span class="sd">        Text is written to the log for the following conditions:</span></div><div class='line' id='LC514'><span class="sd">            XBMC loglevel == -1 (NONE, nothing at all is logged)</span></div><div class='line' id='LC515'><span class="sd">            XBMC loglevel == 0 (NORMAL, shows LOGNOTICE, LOGERROR, LOGSEVERE and LOGFATAL)</span></div><div class='line' id='LC516'><span class="sd">            XBMC loglevel == 1 (DEBUG, shows all)</span></div><div class='line' id='LC517'><span class="sd">        See pydocs for valid values for level.</span></div><div class='line' id='LC518'><br/></div><div class='line' id='LC519'><span class="sd">    Example:</span></div><div class='line' id='LC520'><span class="sd">        xbmc.output(msg=&#39;This is a test string.&#39;, level=xbmc.LOGDEBUG)</span></div><div class='line' id='LC521'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC522'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC523'><br/></div><div class='line' id='LC524'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC525'><span class="k">def</span> <span class="nf">log</span><span class="p">(</span><span class="n">msg</span><span class="p">,</span> <span class="n">level</span><span class="o">=</span><span class="n">LOGNOTICE</span><span class="p">):</span></div><div class='line' id='LC526'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Write a string to XBMC&#39;s log file.</span></div><div class='line' id='LC527'><br/></div><div class='line' id='LC528'><span class="sd">    msg: string - text to output.</span></div><div class='line' id='LC529'><span class="sd">    level: integer - log level to ouput at.</span></div><div class='line' id='LC530'><br/></div><div class='line' id='LC531'><span class="sd">    Note:</span></div><div class='line' id='LC532'><span class="sd">        Text is written to the log for the following conditions.</span></div><div class='line' id='LC533'><span class="sd">            XBMC loglevel == -1 (NONE, nothing at all is logged)</span></div><div class='line' id='LC534'><span class="sd">            XBMC loglevel == 0 (NORMAL, shows LOGNOTICE, LOGERROR, LOGSEVERE and LOGFATAL)</span></div><div class='line' id='LC535'><span class="sd">            XBMC loglevel == 1 (DEBUG, shows all)</span></div><div class='line' id='LC536'><span class="sd">        See pydocs for valid values for level.</span></div><div class='line' id='LC537'><br/></div><div class='line' id='LC538'><span class="sd">    Example:</span></div><div class='line' id='LC539'><span class="sd">        xbmc.log(msg=&#39;This is a test string.&#39;, level=xbmc.LOGDEBUG)</span></div><div class='line' id='LC540'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC541'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC542'><br/></div><div class='line' id='LC543'><span class="k">def</span> <span class="nf">shutdown</span><span class="p">():</span></div><div class='line' id='LC544'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Shutdown the xbox.&quot;&quot;&quot;</span></div><div class='line' id='LC545'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC546'><br/></div><div class='line' id='LC547'><span class="k">def</span> <span class="nf">dashboard</span><span class="p">():</span></div><div class='line' id='LC548'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Boot to dashboard as set in My Pograms/General.&quot;&quot;&quot;</span></div><div class='line' id='LC549'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC550'><br/></div><div class='line' id='LC551'><span class="k">def</span> <span class="nf">restart</span><span class="p">():</span></div><div class='line' id='LC552'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Reboot the xbox.&quot;&quot;&quot;</span></div><div class='line' id='LC553'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC554'><br/></div><div class='line' id='LC555'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC556'><span class="k">def</span> <span class="nf">executescript</span><span class="p">(</span><span class="n">script</span><span class="p">):</span></div><div class='line' id='LC557'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Execute a python script.</span></div><div class='line' id='LC558'><br/></div><div class='line' id='LC559'><span class="sd">    script: string - script filename to execute.</span></div><div class='line' id='LC560'><br/></div><div class='line' id='LC561'><span class="sd">    Example:</span></div><div class='line' id='LC562'><span class="sd">        xbmc.executescript(&#39;special://home/scripts/update.py&#39;)</span></div><div class='line' id='LC563'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC564'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC565'><br/></div><div class='line' id='LC566'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC567'><span class="k">def</span> <span class="nf">executebuiltin</span><span class="p">(</span><span class="n">function</span><span class="p">):</span></div><div class='line' id='LC568'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Execute a built in XBMC function.</span></div><div class='line' id='LC569'><br/></div><div class='line' id='LC570'><span class="sd">    function: string - builtin function to execute.</span></div><div class='line' id='LC571'><br/></div><div class='line' id='LC572'><span class="sd">    List of functions: http://wiki.xbmc.org/?title=List_of_Built_In_Functions</span></div><div class='line' id='LC573'><br/></div><div class='line' id='LC574'><span class="sd">    Example:</span></div><div class='line' id='LC575'><span class="sd">        xbmc.executebuiltin(&#39;XBMC.RunXBE(c:\\\\avalaunch.xbe)&#39;)</span></div><div class='line' id='LC576'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC577'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC578'><br/></div><div class='line' id='LC579'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC580'><span class="k">def</span> <span class="nf">executehttpapi</span><span class="p">(</span><span class="n">httpcommand</span><span class="p">):</span></div><div class='line' id='LC581'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Execute an HTTP API command.</span></div><div class='line' id='LC582'><br/></div><div class='line' id='LC583'><span class="sd">    httpcommand: string - http command to execute.</span></div><div class='line' id='LC584'><br/></div><div class='line' id='LC585'><span class="sd">    List of commands: http://wiki.xbmc.org/?title=WebServerHTTP-API#The_Commands</span></div><div class='line' id='LC586'><br/></div><div class='line' id='LC587'><span class="sd">    Example:</span></div><div class='line' id='LC588'><span class="sd">        response = xbmc.executehttpapi(&#39;TakeScreenShot(special://temp/test.jpg,0,false,200,-1,90)&#39;)</span></div><div class='line' id='LC589'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC590'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC591'><br/></div><div class='line' id='LC592'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC593'><span class="k">def</span> <span class="nf">executeJSONRPC</span><span class="p">(</span><span class="n">jsonrpccommand</span><span class="p">):</span></div><div class='line' id='LC594'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Execute an JSONRPC command.</span></div><div class='line' id='LC595'><br/></div><div class='line' id='LC596'><span class="sd">    jsonrpccommand: string - jsonrpc command to execute.</span></div><div class='line' id='LC597'><br/></div><div class='line' id='LC598'><span class="sd">    List of commands: http://wiki.xbmc.org/index.php?title=JSON_RPC#XBMC_API</span></div><div class='line' id='LC599'><br/></div><div class='line' id='LC600'><span class="sd">    Example:</span></div><div class='line' id='LC601'><span class="sd">        response = xbmc.executeJSONRPC(&#39;{ &quot;jsonrpc&quot;: &quot;2.0&quot;, &quot;method&quot;: &quot;JSONRPC.Introspect&quot;, &quot;id&quot;: 1 }&#39;)</span></div><div class='line' id='LC602'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC603'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC604'><br/></div><div class='line' id='LC605'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC606'><span class="k">def</span> <span class="nf">sleep</span><span class="p">(</span><span class="n">time</span><span class="p">):</span></div><div class='line' id='LC607'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Sleeps for &#39;time&#39; msec.</span></div><div class='line' id='LC608'><br/></div><div class='line' id='LC609'><span class="sd">    time: integer - number of msec to sleep.</span></div><div class='line' id='LC610'><br/></div><div class='line' id='LC611'><span class="sd">    Note:</span></div><div class='line' id='LC612'><span class="sd">        This is useful if you have for example a Player class that is waiting for onPlayBackEnded() calls.</span></div><div class='line' id='LC613'><br/></div><div class='line' id='LC614'><span class="sd">    Raises:</span></div><div class='line' id='LC615'><span class="sd">        TypeError: If time is not an integer.</span></div><div class='line' id='LC616'><br/></div><div class='line' id='LC617'><span class="sd">    Example:</span></div><div class='line' id='LC618'><span class="sd">        xbmc.sleep(2000) # sleeps for 2 seconds</span></div><div class='line' id='LC619'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC620'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC621'><br/></div><div class='line' id='LC622'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC623'><span class="k">def</span> <span class="nf">getLocalizedString</span><span class="p">(</span><span class="nb">id</span><span class="p">):</span></div><div class='line' id='LC624'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a localized &#39;unicode string&#39;.</span></div><div class='line' id='LC625'><br/></div><div class='line' id='LC626'><span class="sd">    id: integer - id# for string you want to localize.</span></div><div class='line' id='LC627'><br/></div><div class='line' id='LC628'><span class="sd">    Note:</span></div><div class='line' id='LC629'><span class="sd">        See strings.xml in \language\{yourlanguage}\ for which id you need for a string.</span></div><div class='line' id='LC630'><br/></div><div class='line' id='LC631'><span class="sd">    Example:</span></div><div class='line' id='LC632'><span class="sd">        locstr = xbmc.getLocalizedString(6)</span></div><div class='line' id='LC633'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC634'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">unicode</span></div><div class='line' id='LC635'><br/></div><div class='line' id='LC636'><span class="k">def</span> <span class="nf">getSkinDir</span><span class="p">():</span></div><div class='line' id='LC637'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the active skin directory as a string.</span></div><div class='line' id='LC638'><br/></div><div class='line' id='LC639'><span class="sd">    Note:</span></div><div class='line' id='LC640'><span class="sd">        This is not the full path like &#39;special://home/addons/MediaCenter&#39;, but only &#39;MediaCenter&#39;.</span></div><div class='line' id='LC641'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC642'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC643'><br/></div><div class='line' id='LC644'><span class="k">def</span> <span class="nf">getLanguage</span><span class="p">():</span></div><div class='line' id='LC645'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the active language as a string.&quot;&quot;&quot;</span></div><div class='line' id='LC646'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC647'><br/></div><div class='line' id='LC648'><span class="k">def</span> <span class="nf">getIPAddress</span><span class="p">():</span></div><div class='line' id='LC649'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the current ip address as a string.&quot;&quot;&quot;</span></div><div class='line' id='LC650'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC651'><br/></div><div class='line' id='LC652'><span class="k">def</span> <span class="nf">getDVDState</span><span class="p">():</span></div><div class='line' id='LC653'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the dvd state as an integer.</span></div><div class='line' id='LC654'><br/></div><div class='line' id='LC655'><span class="sd">    Return values are:</span></div><div class='line' id='LC656'><span class="sd">         1: xbmc.DRIVE_NOT_READY</span></div><div class='line' id='LC657'><span class="sd">        16: xbmc.TRAY_OPEN</span></div><div class='line' id='LC658'><span class="sd">        64: xbmc.TRAY_CLOSED_NO_MEDIA</span></div><div class='line' id='LC659'><span class="sd">        96: xbmc.TRAY_CLOSED_MEDIA_PRESENT</span></div><div class='line' id='LC660'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC661'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">int</span></div><div class='line' id='LC662'><br/></div><div class='line' id='LC663'><span class="k">def</span> <span class="nf">getFreeMem</span><span class="p">():</span></div><div class='line' id='LC664'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the amount of free memory in MB as an integer.&quot;&quot;&quot;</span></div><div class='line' id='LC665'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">int</span></div><div class='line' id='LC666'><br/></div><div class='line' id='LC667'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC668'><span class="k">def</span> <span class="nf">getInfoLabel</span><span class="p">(</span><span class="n">infotag</span><span class="p">):</span></div><div class='line' id='LC669'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns an InfoLabel as a string.</span></div><div class='line' id='LC670'><br/></div><div class='line' id='LC671'><span class="sd">    infotag: string - infoTag for value you want returned.</span></div><div class='line' id='LC672'><br/></div><div class='line' id='LC673'><span class="sd">    List of InfoTags - http://wiki.xbmc.org/?title=InfoLabels</span></div><div class='line' id='LC674'><br/></div><div class='line' id='LC675'><span class="sd">    Example:</span></div><div class='line' id='LC676'><span class="sd">        label = xbmc.getInfoLabel(&#39;Weather.Conditions&#39;)</span></div><div class='line' id='LC677'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC678'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC679'><br/></div><div class='line' id='LC680'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC681'><span class="k">def</span> <span class="nf">getInfoImage</span><span class="p">(</span><span class="n">infotag</span><span class="p">):</span></div><div class='line' id='LC682'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a filename including path to the InfoImage&#39;s thumbnail as a string.</span></div><div class='line' id='LC683'><br/></div><div class='line' id='LC684'><span class="sd">    infotag: string - infotag for value you want returned.</span></div><div class='line' id='LC685'><br/></div><div class='line' id='LC686'><span class="sd">    List of InfoTags - http://wiki.xbmc.org/?title=InfoLabels</span></div><div class='line' id='LC687'><br/></div><div class='line' id='LC688'><span class="sd">    Example:</span></div><div class='line' id='LC689'><span class="sd">        filename = xbmc.getInfoImage(&#39;Weather.Conditions&#39;)</span></div><div class='line' id='LC690'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC691'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC692'><br/></div><div class='line' id='LC693'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC694'><span class="k">def</span> <span class="nf">playSFX</span><span class="p">(</span><span class="n">filename</span><span class="p">):</span></div><div class='line' id='LC695'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Plays a wav file by filename.</span></div><div class='line' id='LC696'><br/></div><div class='line' id='LC697'><span class="sd">    filename: string - filename of the wav file to play.</span></div><div class='line' id='LC698'><br/></div><div class='line' id='LC699'><span class="sd">    Example:</span></div><div class='line' id='LC700'><span class="sd">        xbmc.playSFX(&#39;special://xbmc/scripts/dingdong.wav&#39;)</span></div><div class='line' id='LC701'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC702'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC703'><br/></div><div class='line' id='LC704'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC705'><span class="k">def</span> <span class="nf">enableNavSounds</span><span class="p">(</span><span class="n">yesNo</span><span class="p">):</span></div><div class='line' id='LC706'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Enables/Disables nav sounds.</span></div><div class='line' id='LC707'><br/></div><div class='line' id='LC708'><span class="sd">    yesNo: integer - enable (True) or disable (False) nav sounds</span></div><div class='line' id='LC709'><br/></div><div class='line' id='LC710'><span class="sd">    Example:</span></div><div class='line' id='LC711'><span class="sd">        xbmc.enableNavSounds(True)</span></div><div class='line' id='LC712'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC713'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC714'><br/></div><div class='line' id='LC715'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC716'><span class="k">def</span> <span class="nf">getCondVisibility</span><span class="p">(</span><span class="n">condition</span><span class="p">):</span></div><div class='line' id='LC717'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns True (1) or False (0) as a bool.</span></div><div class='line' id='LC718'><br/></div><div class='line' id='LC719'><span class="sd">    condition: string - condition to check.</span></div><div class='line' id='LC720'><br/></div><div class='line' id='LC721'><span class="sd">    List of Conditions - http://wiki.xbmc.org/?title=List_of_Boolean_Conditions</span></div><div class='line' id='LC722'><br/></div><div class='line' id='LC723'><span class="sd">    Note:</span></div><div class='line' id='LC724'><span class="sd">        You can combine two (or more) of the above settings by using &quot;+&quot; as an AND operator,</span></div><div class='line' id='LC725'><span class="sd">        &quot;|&quot; as an OR operator, &quot;!&quot; as a NOT operator, and &quot;[&quot; and &quot;]&quot; to bracket expressions.</span></div><div class='line' id='LC726'><br/></div><div class='line' id='LC727'><span class="sd">    Example:</span></div><div class='line' id='LC728'><span class="sd">        visible = xbmc.getCondVisibility(&#39;[Control.IsVisible(41) + !Control.IsVisible(12)]&#39;)</span></div><div class='line' id='LC729'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC730'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">bool</span></div><div class='line' id='LC731'><br/></div><div class='line' id='LC732'><span class="k">def</span> <span class="nf">getGlobalIdleTime</span><span class="p">():</span></div><div class='line' id='LC733'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the elapsed idle time in seconds as an integer.&quot;&quot;&quot;</span></div><div class='line' id='LC734'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">int</span></div><div class='line' id='LC735'><br/></div><div class='line' id='LC736'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC737'><span class="k">def</span> <span class="nf">getCacheThumbName</span><span class="p">(</span><span class="n">path</span><span class="p">):</span></div><div class='line' id='LC738'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a thumb cache filename.</span></div><div class='line' id='LC739'><br/></div><div class='line' id='LC740'><span class="sd">    path: string or unicode - path to file</span></div><div class='line' id='LC741'><br/></div><div class='line' id='LC742'><span class="sd">    Example:</span></div><div class='line' id='LC743'><span class="sd">        thumb = xbmc.getCacheThumbName(&#39;f:\\videos\\movie.avi&#39;)</span></div><div class='line' id='LC744'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC745'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC746'><br/></div><div class='line' id='LC747'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC748'><span class="k">def</span> <span class="nf">makeLegalFilename</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">fatX</span><span class="o">=</span><span class="bp">True</span><span class="p">):</span></div><div class='line' id='LC749'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a legal filename or path as a string.</span></div><div class='line' id='LC750'><br/></div><div class='line' id='LC751'><span class="sd">    filename: string or unicode - filename/path to make legal</span></div><div class='line' id='LC752'><span class="sd">    fatX: bool - True=Xbox file system</span></div><div class='line' id='LC753'><br/></div><div class='line' id='LC754'><span class="sd">    Note:</span></div><div class='line' id='LC755'><span class="sd">        If fatX is true you should pass a full path. If fatX is false only pass the basename of the path.</span></div><div class='line' id='LC756'><br/></div><div class='line' id='LC757'><span class="sd">    Example:</span></div><div class='line' id='LC758'><span class="sd">        filename = xbmc.makeLegalFilename(&#39;F:\\Trailers\\Ice Age: The Meltdown.avi&#39;)</span></div><div class='line' id='LC759'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC760'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC761'><br/></div><div class='line' id='LC762'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC763'><span class="k">def</span> <span class="nf">translatePath</span><span class="p">(</span><span class="n">path</span><span class="p">):</span></div><div class='line' id='LC764'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the translated path.</span></div><div class='line' id='LC765'><br/></div><div class='line' id='LC766'><span class="sd">    path: string or unicode - Path to format</span></div><div class='line' id='LC767'><br/></div><div class='line' id='LC768'><span class="sd">    Note:</span></div><div class='line' id='LC769'><span class="sd">        Only useful if you are coding for both Linux and Windows/Xbox.</span></div><div class='line' id='LC770'><span class="sd">        e.g. Converts &#39;special://masterprofile/script_data&#39; -&gt; &#39;/home/user/XBMC/UserData/script_data&#39;</span></div><div class='line' id='LC771'><span class="sd">        on Linux. Would return &#39;special://masterprofile/script_data&#39; on the Xbox.</span></div><div class='line' id='LC772'><br/></div><div class='line' id='LC773'><span class="sd">    Example:</span></div><div class='line' id='LC774'><span class="sd">        fpath = xbmc.translatePath(&#39;special://masterprofile/script_data&#39;)</span></div><div class='line' id='LC775'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC776'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC777'><br/></div><div class='line' id='LC778'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC779'><span class="k">def</span> <span class="nf">getCleanMovieTitle</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">usefoldername</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span></div><div class='line' id='LC780'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns a clean movie title and year string if available.</span></div><div class='line' id='LC781'><br/></div><div class='line' id='LC782'><span class="sd">    path: string or unicode - String to clean</span></div><div class='line' id='LC783'><span class="sd">    &quot;usefoldername: bool - use folder names</span></div><div class='line' id='LC784'><br/></div><div class='line' id='LC785'><span class="sd">    Example:</span></div><div class='line' id='LC786'><span class="sd">        title, year = xbmc.getCleanMovieTitle(&#39;/path/to/moviefolder/test.avi&#39;, True)</span></div><div class='line' id='LC787'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC788'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC789'><br/></div><div class='line' id='LC790'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC791'><span class="k">def</span> <span class="nf">validatePath</span><span class="p">(</span><span class="n">path</span><span class="p">):</span></div><div class='line' id='LC792'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the validated path.</span></div><div class='line' id='LC793'><br/></div><div class='line' id='LC794'><span class="sd">    path: string or unicode - Path to format</span></div><div class='line' id='LC795'><br/></div><div class='line' id='LC796'><span class="sd">    Note:</span></div><div class='line' id='LC797'><span class="sd">        Only useful if you are coding for both Linux and Windows/Xbox for fixing slash problems.</span></div><div class='line' id='LC798'><span class="sd">        e.g. Corrects &#39;Z://something&#39; -&gt; &#39;Z:\\something&#39;</span></div><div class='line' id='LC799'><br/></div><div class='line' id='LC800'><span class="sd">    Example:</span></div><div class='line' id='LC801'><span class="sd">        fpath = xbmc.validatePath(somepath)</span></div><div class='line' id='LC802'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC803'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC804'><br/></div><div class='line' id='LC805'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC806'><span class="k">def</span> <span class="nf">getRegion</span><span class="p">(</span><span class="nb">id</span><span class="p">):</span></div><div class='line' id='LC807'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns your regions setting as a string for the specified id.</span></div><div class='line' id='LC808'><br/></div><div class='line' id='LC809'><span class="sd">    id: string - id of setting to return</span></div><div class='line' id='LC810'><br/></div><div class='line' id='LC811'><span class="sd">    Note:</span></div><div class='line' id='LC812'><span class="sd">        Choices are (dateshort, datelong, time, meridiem, tempunit, speedunit)</span></div><div class='line' id='LC813'><br/></div><div class='line' id='LC814'><span class="sd">    Example:</span></div><div class='line' id='LC815'><span class="sd">        date_long_format = xbmc.getRegion(&#39;datelong&#39;)</span></div><div class='line' id='LC816'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC817'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC818'><br/></div><div class='line' id='LC819'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC820'><span class="k">def</span> <span class="nf">getSupportedMedia</span><span class="p">(</span><span class="n">media</span><span class="p">):</span></div><div class='line' id='LC821'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the supported file types for the specific media as a string.</span></div><div class='line' id='LC822'><br/></div><div class='line' id='LC823'><span class="sd">    media: string - media type</span></div><div class='line' id='LC824'><br/></div><div class='line' id='LC825'><span class="sd">    Note:</span></div><div class='line' id='LC826'><span class="sd">        Media type can be (video, music, picture).</span></div><div class='line' id='LC827'><br/></div><div class='line' id='LC828'><span class="sd">        The return value is a pipe separated string of filetypes (eg. &#39;.mov|.avi&#39;).</span></div><div class='line' id='LC829'><br/></div><div class='line' id='LC830'><span class="sd">    Example:</span></div><div class='line' id='LC831'><span class="sd">        mTypes = xbmc.getSupportedMedia(&#39;video&#39;)</span></div><div class='line' id='LC832'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC833'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC834'><br/></div><div class='line' id='LC835'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC836'><span class="k">def</span> <span class="nf">skinHasImage</span><span class="p">(</span><span class="n">image</span><span class="p">):</span></div><div class='line' id='LC837'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns True if the image file exists in the skin.</span></div><div class='line' id='LC838'><br/></div><div class='line' id='LC839'><span class="sd">    image: string - image filename</span></div><div class='line' id='LC840'><br/></div><div class='line' id='LC841'><span class="sd">    Note:</span></div><div class='line' id='LC842'><span class="sd">        If the media resides in a subfolder include it. (eg. home-myfiles\\home-myfiles2.png)</span></div><div class='line' id='LC843'><br/></div><div class='line' id='LC844'><span class="sd">    Example:</span></div><div class='line' id='LC845'><span class="sd">        exists = xbmc.skinHasImage(&#39;ButtonFocusedTexture.png&#39;)</span></div><div class='line' id='LC846'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC847'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">bool</span></div><div class='line' id='LC848'><br/></div><div class='line' id='LC849'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC850'><span class="k">def</span> <span class="nf">subHashAndFileSize</span><span class="p">(</span><span class="nb">file</span><span class="p">):</span></div><div class='line' id='LC851'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns tuple with subtitle hash and size.</span></div><div class='line' id='LC852'><br/></div><div class='line' id='LC853'><span class="sd">    file: string - file to calculate hash and size for</span></div><div class='line' id='LC854'><br/></div><div class='line' id='LC855'><span class="sd">    Example:</span></div><div class='line' id='LC856'><span class="sd">        size,hash = xbmc.subHashAndFileSize(file)</span></div><div class='line' id='LC857'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC858'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">tuple</span></div></pre></div>
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
      <li>&copy; 2013 <span title="0.05151s from fe3.rs.github.com">GitHub</span>, Inc.</li>
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

