<script src="https://www.google.com/jsapi?key=ABQIAAAAFEyVt-pBJaTXzM__EKlCrBTsyyvZhuBjP1YLRoRPwle1bnzSQRQBJp693I-9cLRWqwHDWCO_xmGezQ"
    type="text/javascript"></script>
<script type="text/javascript">
    google.load("search", "1", {"language" : "en"});

    // Call this function when the page has been loaded
    function initialize() {
        alert("fsd")
        var searchControl = new google.search.SearchControl();

        // site restricted web search
        /*
        var siteSearch = new google.search.WebSearch();
        siteSearch.setUserDefinedLabel("jquery4u.com");
        siteSearch.setUserDefinedClassSuffix("siteSearch");
        siteSearch.setSiteRestriction("jquery4u.com");
        searchControl.addSearcher(siteSearch);
        */

        // Search API Topics
        //searchControl.addSearcher(new google.search.WebSearch());
        //searchControl.addSearcher(new google.search.NewsSearch());
        //searchControl.addSearcher(new google.search.BlogSearch());
        //searchControl.addSearcher(new google.search.ImageSearch());
        searchControl.addSearcher(new google.search.BookSearch());
        //searchControl.addSearcher(new google.search.VideoSearch());
        // others
        //searchControl.addSearcher(new google.search.LocalSearch());
        //searchControl.addSearcher(new google.search.PatentSearch());

        // create a drawOptions object
        var drawOptions = new google.search.DrawOptions();
        // tell the searcher to draw itself in tabbed mode
        drawOptions.setDrawMode(google.search.SearchControl.DRAW_MODE_TABBED);
        searchControl.draw(document.getElementById("searchcontrol"), drawOptions);
    }
    google.setOnLoadCallback(initialize);
</script>

<style type="text/css">
    /* the width of the controls (keep same as gsc-results for flush look) */
    #searchcontrol { width:600px; }
    .gsc-control { width:600px; }
    /* the width of the search results box; no height value = nice auto look */
    .gsc-results { width:600px; }
    /* the width of the search input */
    .gsc-input { width:20px; }
    /* hide "powered by google" (optional) */
    .gsc-branding { display:none; }
    .gs-title a { color:orange; font-weight:bold; }
    #searchcontrol a { color:orange; }
</style>