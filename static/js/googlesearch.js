// Call this function when the page has been loaded
function initialize() {
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
