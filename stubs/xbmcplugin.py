


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>xbmcstubs/xbmcplugin.py at master · Tenzer/xbmcstubs · GitHub</title>
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

        <link data-pjax-transient rel='permalink' href='/Tenzer/xbmcstubs/blob/be31664f64468bf4d03bdcc2a521aa0418591094/xbmcplugin.py'>
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
      <a class="button" href="/login?return_to=%2FTenzer%2Fxbmcstubs%2Fblob%2Fmaster%2Fxbmcplugin.py">Sign in</a>
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
          


<!-- blob contrib key: blob_contributors:v21:64aa032c3d29832468575a1d527f8678 -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:64aa032c3d29832468575a1d527f8678 -->

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
              <a href="/Tenzer/xbmcstubs/blob/Dharma/xbmcplugin.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="Dharma" data-skip-pjax="true" rel="nofollow" title="Dharma">Dharma</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Tenzer/xbmcstubs/blob/master/xbmcplugin.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" data-skip-pjax="true" rel="nofollow" title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/Tenzer/xbmcstubs/blob/Dharma.01/xbmcplugin.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="Dharma.01" data-skip-pjax="true" rel="nofollow" title="Dharma.01">Dharma.01</a>
            </div> <!-- /.select-menu-item -->
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/Tenzer/xbmcstubs" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">xbmcstubs</span></a></span></span><span class="separator"> / </span><strong class="final-path">xbmcplugin.py</strong> <span class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="xbmcplugin.py" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


  <div class="commit commit-loader file-history-tease js-deferred-content" data-url="/Tenzer/xbmcstubs/contributors/master/xbmcplugin.py">
    Fetching contributors…

    <div class="participation">
      <p class="loader-loading"><img alt="Octocat-spinner-32-eaf2f5" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" /></p>
      <p class="loader-error">Cannot retrieve contributors at this time</p>
    </div>
  </div>

<div id="files" class="bubble">
  <div class="file">
    <div class="meta">
      <div class="info">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">file</span>
          <span>201 lines (158 sloc)</span>
        <span>6.655 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
              <a class="minibutton js-entice" href=""
                 data-entice="You must be signed in to make or propose changes">Edit</a>
          <a href="/Tenzer/xbmcstubs/raw/master/xbmcplugin.py" class="button minibutton " id="raw-url">Raw</a>
            <a href="/Tenzer/xbmcstubs/blame/master/xbmcplugin.py" class="button minibutton ">Blame</a>
          <a href="/Tenzer/xbmcstubs/commits/master/xbmcplugin.py" class="button minibutton " rel="nofollow">History</a>
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

          </td>
          <td class="blob-line-code">
                  <div class="highlight"><pre><div class='line' id='LC1'><span class="n">SORT_METHOD_NONE</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC2'><span class="n">SORT_METHOD_LABEL</span> <span class="o">=</span> <span class="mi">1</span></div><div class='line' id='LC3'><span class="n">SORT_METHOD_LABEL_IGNORE_THE</span> <span class="o">=</span> <span class="mi">2</span></div><div class='line' id='LC4'><span class="n">SORT_METHOD_DATE</span> <span class="o">=</span> <span class="mi">3</span></div><div class='line' id='LC5'><span class="n">SORT_METHOD_SIZE</span> <span class="o">=</span> <span class="mi">4</span></div><div class='line' id='LC6'><span class="n">SORT_METHOD_FILE</span> <span class="o">=</span> <span class="mi">5</span></div><div class='line' id='LC7'><span class="n">SORT_METHOD_DRIVE_TYPE</span> <span class="o">=</span> <span class="mi">6</span></div><div class='line' id='LC8'><span class="n">SORT_METHOD_TRACKNUM</span> <span class="o">=</span> <span class="mi">7</span></div><div class='line' id='LC9'><span class="n">SORT_METHOD_DURATION</span> <span class="o">=</span> <span class="mi">8</span></div><div class='line' id='LC10'><span class="n">SORT_METHOD_TITLE</span> <span class="o">=</span> <span class="mi">9</span></div><div class='line' id='LC11'><span class="n">SORT_METHOD_TITLE_IGNORE_THE</span> <span class="o">=</span> <span class="mi">10</span></div><div class='line' id='LC12'><span class="n">SORT_METHOD_ARTIST</span> <span class="o">=</span> <span class="mi">11</span></div><div class='line' id='LC13'><span class="n">SORT_METHOD_ARTIST_IGNORE_THE</span> <span class="o">=</span> <span class="mi">12</span></div><div class='line' id='LC14'><span class="n">SORT_METHOD_ALBUM</span> <span class="o">=</span> <span class="mi">13</span></div><div class='line' id='LC15'><span class="n">SORT_METHOD_ALBUM_IGNORE_THE</span> <span class="o">=</span> <span class="mi">14</span></div><div class='line' id='LC16'><span class="n">SORT_METHOD_GENRE</span> <span class="o">=</span> <span class="mi">15</span></div><div class='line' id='LC17'><span class="n">SORT_METHOD_VIDEO_YEAR</span> <span class="o">=</span><span class="mi">16</span></div><div class='line' id='LC18'><span class="n">SORT_METHOD_VIDEO_RATING</span> <span class="o">=</span> <span class="mi">17</span></div><div class='line' id='LC19'><br/></div><div class='line' id='LC20'><span class="n">SORT_METHOD_PROGRAM_COUNT</span> <span class="o">=</span> <span class="mi">20</span></div><div class='line' id='LC21'><span class="n">SORT_METHOD_PLAYLIST_ORDER</span> <span class="o">=</span> <span class="mi">21</span></div><div class='line' id='LC22'><span class="n">SORT_METHOD_EPISODE</span> <span class="o">=</span> <span class="mi">22</span></div><div class='line' id='LC23'><span class="n">SORT_METHOD_VIDEO_TITLE</span> <span class="o">=</span> <span class="mi">23</span></div><div class='line' id='LC24'><br/></div><div class='line' id='LC25'><span class="n">SORT_METHOD_PRODUCTIONCODE</span> <span class="o">=</span> <span class="mi">26</span></div><div class='line' id='LC26'><span class="n">SORT_METHOD_SONG_RATING</span> <span class="o">=</span> <span class="mi">27</span></div><div class='line' id='LC27'><span class="n">SORT_METHOD_MPAA_RATING</span> <span class="o">=</span> <span class="mi">28</span></div><div class='line' id='LC28'><span class="n">SORT_METHOD_VIDEO_RUNTIME</span> <span class="o">=</span> <span class="mi">29</span></div><div class='line' id='LC29'><span class="n">SORT_METHOD_STUDIO</span> <span class="o">=</span> <span class="mi">30</span></div><div class='line' id='LC30'><span class="n">SORT_METHOD_STUDIO_IGNORE_THE</span> <span class="o">=</span> <span class="mi">31</span></div><div class='line' id='LC31'><br/></div><div class='line' id='LC32'><span class="n">SORT_METHOD_LISTENERS</span> <span class="o">=</span> <span class="mi">36</span></div><div class='line' id='LC33'><span class="n">SORT_METHOD_UNSORTED</span> <span class="o">=</span> <span class="mi">37</span></div><div class='line' id='LC34'><br/></div><div class='line' id='LC35'><span class="n">SORT_METHOD_BITRATE</span> <span class="o">=</span> <span class="mi">39</span></div><div class='line' id='LC36'><br/></div><div class='line' id='LC37'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC38'><span class="k">def</span> <span class="nf">addDirectoryItem</span><span class="p">(</span><span class="n">handle</span><span class="p">,</span> <span class="n">url</span><span class="p">,</span> <span class="n">listitem</span><span class="p">,</span> <span class="n">isFolder</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">totalItems</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span></div><div class='line' id='LC39'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Callback function to pass directory contents back to XBMC.</span></div><div class='line' id='LC40'><br/></div><div class='line' id='LC41'><span class="sd">    Returns a bool for successful completion.</span></div><div class='line' id='LC42'><br/></div><div class='line' id='LC43'><span class="sd">    handle: integer - handle the plugin was started with.</span></div><div class='line' id='LC44'><span class="sd">    url: string - url of the entry. would be plugin:// for another virtual directory.</span></div><div class='line' id='LC45'><span class="sd">    listitem: ListItem - item to add.</span></div><div class='line' id='LC46'><span class="sd">    isFolder: bool - True=folder / False=not a folder.</span></div><div class='line' id='LC47'><span class="sd">    totalItems: integer - total number of items that will be passed. (used for progressbar)</span></div><div class='line' id='LC48'><br/></div><div class='line' id='LC49'><span class="sd">    Example:</span></div><div class='line' id='LC50'><span class="sd">        if not xbmcplugin.addDirectoryItem(int(sys.argv[1]), &#39;F:\\Trailers\\300.mov&#39;, listitem, totalItems=50):</span></div><div class='line' id='LC51'><span class="sd">            break</span></div><div class='line' id='LC52'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">bool</span></div><div class='line' id='LC54'><br/></div><div class='line' id='LC55'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC56'><span class="k">def</span> <span class="nf">addDirectoryItems</span><span class="p">(</span><span class="n">handle</span><span class="p">,</span> <span class="n">items</span><span class="p">,</span> <span class="n">totalItems</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span></div><div class='line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Callback function to pass directory contents back to XBMC as a list.</span></div><div class='line' id='LC58'><br/></div><div class='line' id='LC59'><span class="sd">    Returns a bool for successful completion.</span></div><div class='line' id='LC60'><br/></div><div class='line' id='LC61'><span class="sd">    handle: integer - handle the plugin was started with.</span></div><div class='line' id='LC62'><span class="sd">    items: List - list of (url, listitem[, isFolder]) as a tuple to add.</span></div><div class='line' id='LC63'><span class="sd">    totalItems: integer - total number of items that will be passed. (used for progressbar)</span></div><div class='line' id='LC64'><br/></div><div class='line' id='LC65'><span class="sd">    Note:</span></div><div class='line' id='LC66'><span class="sd">        Large lists benefit over using the standard addDirectoryItem().</span></div><div class='line' id='LC67'><span class="sd">        You may call this more than once to add items in chunks.</span></div><div class='line' id='LC68'><br/></div><div class='line' id='LC69'><span class="sd">    Example:</span></div><div class='line' id='LC70'><span class="sd">        if not xbmcplugin.addDirectoryItems(int(sys.argv[1]), [(url, listitem, False,)]:</span></div><div class='line' id='LC71'><span class="sd">            raise</span></div><div class='line' id='LC72'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">bool</span></div><div class='line' id='LC74'><br/></div><div class='line' id='LC75'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC76'><span class="k">def</span> <span class="nf">endOfDirectory</span><span class="p">(</span><span class="n">handle</span><span class="p">,</span> <span class="n">succeeded</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">updateListing</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">cacheToDisc</span><span class="o">=</span><span class="bp">True</span><span class="p">):</span></div><div class='line' id='LC77'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Callback function to tell XBMC that the end of the directory listing in a virtualPythonFolder module is reached.</span></div><div class='line' id='LC78'><br/></div><div class='line' id='LC79'><span class="sd">    handle: integer - handle the plugin was started with.</span></div><div class='line' id='LC80'><span class="sd">    succeeded: bool - True=script completed successfully/False=Script did not.</span></div><div class='line' id='LC81'><span class="sd">    updateListing: bool - True=this folder should update the current listing/False=Folder is a subfolder.</span></div><div class='line' id='LC82'><span class="sd">    cacheToDisc: bool - True=Folder will cache if extended time/False=this folder will never cache to disc.</span></div><div class='line' id='LC83'><br/></div><div class='line' id='LC84'><span class="sd">    Example:</span></div><div class='line' id='LC85'><span class="sd">        xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=False)</span></div><div class='line' id='LC86'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC88'><br/></div><div class='line' id='LC89'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC90'><span class="k">def</span> <span class="nf">setResolvedUrl</span><span class="p">(</span><span class="n">handle</span><span class="p">,</span> <span class="n">succeeded</span><span class="p">,</span> <span class="n">listitem</span><span class="p">):</span></div><div class='line' id='LC91'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Callback function to tell XBMC that the file plugin has been resolved to a url</span></div><div class='line' id='LC92'><br/></div><div class='line' id='LC93'><span class="sd">    handle: integer - handle the plugin was started with.</span></div><div class='line' id='LC94'><span class="sd">    succeeded: bool - True=script completed successfully/False=Script did not.</span></div><div class='line' id='LC95'><span class="sd">    listitem: ListItem - item the file plugin resolved to for playback.</span></div><div class='line' id='LC96'><br/></div><div class='line' id='LC97'><span class="sd">    Example:</span></div><div class='line' id='LC98'><span class="sd">        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)</span></div><div class='line' id='LC99'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC100'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC101'><br/></div><div class='line' id='LC102'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC103'><span class="k">def</span> <span class="nf">addSortMethod</span><span class="p">(</span><span class="n">handle</span><span class="p">,</span> <span class="n">sortMethod</span><span class="p">,</span> <span class="n">label2</span><span class="o">=</span><span class="s">&quot;%D&quot;</span><span class="p">):</span></div><div class='line' id='LC104'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Adds a sorting method for the media list.</span></div><div class='line' id='LC105'><br/></div><div class='line' id='LC106'><span class="sd">    handle: integer - handle the plugin was started with.</span></div><div class='line' id='LC107'><span class="sd">    sortMethod: integer - number for sortmethod see FileItem.h.</span></div><div class='line' id='LC108'><span class="sd">    label2Mask: string - the label mask to use for the second label.  Defaults to &#39;%D&#39;</span></div><div class='line' id='LC109'><span class="sd">        applies to: SORT_METHOD_NONE, SORT_METHOD_UNSORTED, SORT_METHOD_VIDEO_TITLE,</span></div><div class='line' id='LC110'><span class="sd">        SORT_METHOD_TRACKNUM, SORT_METHOD_FILE, SORT_METHOD_TITLE</span></div><div class='line' id='LC111'><span class="sd">        SORT_METHOD_TITLE_IGNORE_THE, SORT_METHOD_LABEL</span></div><div class='line' id='LC112'><span class="sd">        SORT_METHOD_LABEL_IGNORE_THE</span></div><div class='line' id='LC113'><br/></div><div class='line' id='LC114'><span class="sd">    Example:</span></div><div class='line' id='LC115'><span class="sd">        xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE)</span></div><div class='line' id='LC116'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC117'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC118'><br/></div><div class='line' id='LC119'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC120'><span class="k">def</span> <span class="nf">getSetting</span><span class="p">(</span><span class="n">handle</span><span class="p">,</span> <span class="nb">id</span><span class="p">):</span></div><div class='line' id='LC121'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Returns the value of a setting as a string.</span></div><div class='line' id='LC122'><br/></div><div class='line' id='LC123'><span class="sd">    handle: integer - handle the plugin was started with.</span></div><div class='line' id='LC124'><span class="sd">    id: string - id of the setting that the module needs to access.</span></div><div class='line' id='LC125'><br/></div><div class='line' id='LC126'><span class="sd">    Example:</span></div><div class='line' id='LC127'><span class="sd">        apikey = xbmcplugin.getSetting(int(sys.argv[1]), &#39;apikey&#39;)</span></div><div class='line' id='LC128'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">str</span></div><div class='line' id='LC130'><br/></div><div class='line' id='LC131'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC132'><span class="k">def</span> <span class="nf">setSetting</span><span class="p">(</span><span class="n">handle</span><span class="p">,</span> <span class="nb">id</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Sets a plugin setting for the current running plugin.</span></div><div class='line' id='LC134'><br/></div><div class='line' id='LC135'><span class="sd">    handle: integer - handle the plugin was started with.</span></div><div class='line' id='LC136'><span class="sd">    id: string - id of the setting that the module needs to access.</span></div><div class='line' id='LC137'><span class="sd">    value: string or unicode - value of the setting.</span></div><div class='line' id='LC138'><br/></div><div class='line' id='LC139'><span class="sd">    Example:</span></div><div class='line' id='LC140'><span class="sd">        xbmcplugin.setSetting(int(sys.argv[1]), id=&#39;username&#39;, value=&#39;teamxbmc&#39;)</span></div><div class='line' id='LC141'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC142'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC143'><br/></div><div class='line' id='LC144'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC145'><span class="k">def</span> <span class="nf">setContent</span><span class="p">(</span><span class="n">handle</span><span class="p">,</span> <span class="n">content</span><span class="p">):</span></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Sets the plugins content.</span></div><div class='line' id='LC147'><br/></div><div class='line' id='LC148'><span class="sd">    handle: integer - handle the plugin was started with.</span></div><div class='line' id='LC149'><span class="sd">    content: string - content type (eg. movies).</span></div><div class='line' id='LC150'><br/></div><div class='line' id='LC151'><span class="sd">    Note:</span></div><div class='line' id='LC152'><span class="sd">        Possible values for content: files, songs, artists, albums, movies, tvshows, episodes, musicvideos</span></div><div class='line' id='LC153'><br/></div><div class='line' id='LC154'><span class="sd">    Example:</span></div><div class='line' id='LC155'><span class="sd">        xbmcplugin.setContent(int(sys.argv[1]), &#39;movies&#39;)</span></div><div class='line' id='LC156'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC157'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC158'><br/></div><div class='line' id='LC159'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC160'><span class="k">def</span> <span class="nf">setPluginCategory</span><span class="p">(</span><span class="n">handle</span><span class="p">,</span> <span class="n">category</span><span class="p">):</span></div><div class='line' id='LC161'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Sets the plugins name for skins to display.</span></div><div class='line' id='LC162'><br/></div><div class='line' id='LC163'><span class="sd">    handle: integer - handle the plugin was started with.</span></div><div class='line' id='LC164'><span class="sd">    category: string or unicode - plugins sub category.</span></div><div class='line' id='LC165'><br/></div><div class='line' id='LC166'><span class="sd">    Example:</span></div><div class='line' id='LC167'><span class="sd">        xbmcplugin.setPluginCategory(int(sys.argv[1]), &#39;Comedy&#39;)</span></div><div class='line' id='LC168'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC169'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC170'><br/></div><div class='line' id='LC171'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC172'><span class="k">def</span> <span class="nf">setPluginFanart</span><span class="p">(</span><span class="n">handle</span><span class="p">,</span> <span class="n">image</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">color1</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">color2</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">color3</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC173'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Sets the plugins fanart and color for skins to display.</span></div><div class='line' id='LC174'><br/></div><div class='line' id='LC175'><span class="sd">    handle: integer - handle the plugin was started with.\n&quot;</span></div><div class='line' id='LC176'><span class="sd">    image: string - path to fanart image.</span></div><div class='line' id='LC177'><span class="sd">    color1: hexstring - color1. (e.g. &#39;0xFFFFFFFF&#39;)</span></div><div class='line' id='LC178'><span class="sd">    color2: hexstring - color2. (e.g. &#39;0xFFFF3300&#39;)</span></div><div class='line' id='LC179'><span class="sd">    color3: hexstring - color3. (e.g. &#39;0xFF000000&#39;)</span></div><div class='line' id='LC180'><br/></div><div class='line' id='LC181'><span class="sd">    Example:</span></div><div class='line' id='LC182'><span class="sd">        xbmcplugin.setPluginFanart(int(sys.argv[1]), &#39;special://home/addons/plugins/video/Apple movie trailers II/fanart.png&#39;, color2=&#39;0xFFFF3300&#39;)</span></div><div class='line' id='LC183'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC184'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC185'><br/></div><div class='line' id='LC186'><span class="c">#noinspection PyUnusedLocal</span></div><div class='line' id='LC187'><span class="k">def</span> <span class="nf">setProperty</span><span class="p">(</span><span class="n">handle</span><span class="p">,</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span></div><div class='line' id='LC188'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Sets a container property for this plugin.</span></div><div class='line' id='LC189'><br/></div><div class='line' id='LC190'><span class="sd">    handle: integer - handle the plugin was started with.</span></div><div class='line' id='LC191'><span class="sd">    key: string - property name.</span></div><div class='line' id='LC192'><span class="sd">    value: string or unicode - value of property.</span></div><div class='line' id='LC193'><br/></div><div class='line' id='LC194'><span class="sd">    Note:</span></div><div class='line' id='LC195'><span class="sd">        Key is NOT case sensitive.</span></div><div class='line' id='LC196'><br/></div><div class='line' id='LC197'><span class="sd">    Example:</span></div><div class='line' id='LC198'><span class="sd">        xbmcplugin.setProperty(int(sys.argv[1]), &#39;Emulator&#39;, &#39;M.A.M.E.&#39;)</span></div><div class='line' id='LC199'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC200'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div></pre></div>
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
      <li>&copy; 2013 <span title="0.07663s from fe3.rs.github.com">GitHub</span>, Inc.</li>
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

