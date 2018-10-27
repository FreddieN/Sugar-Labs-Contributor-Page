var contributors = [];
var phtml = "";
var mhtml = "";
var min1 = 0;
var max1 = 20;
var lastupdated = "";
$.getJSON( "clists.json", function( data ) {
        contributors = data['opensource'];
        members = data['members']
        lastupdated = data['dategen'];
});
$( document ).ready(function() {
        if(screen.width < 920) {
            mpids = 2;
        } else {
            mpids = 4;
        }
        if(min1 === 0) { $("#mback").prop("disabled", true);};
        var profileid = 0;
        $.each(contributors, function(i, item) {
                if (profileid % 5 === 0) {phtml += "</div><div class='row top-buffer'>";}
                phtml += "<div class='col-sm text-center'>";
                phtml += "<a target='_blank' href='https://github.com/"+i+"'>";
                phtml += "<img class='bigpimage' src='https://avatars.githubusercontent.com/"+i+"'>";
                phtml += '<div class="container">';
                phtml += '<strong class="bpn">@'+i+'</strong>';
                phtml += '</div></a></div>'
                profileid++;
        });
        var profileid = 0;
        $.each(members, function(i, item) {
            if(profileid < max1 && profileid >= min1) {
                if (profileid % mpids === 0) {mhtml += "</div><div class='row'>";}
                    mhtml += "<div class='mlistp col text-center'><p>"+i+"</p></div>";
                    
                }
            profileid++;
    });
        phtml += "</div><br><br> <p class='lastupdated text-center'>Last updated: "+lastupdated+"</p>"
        document.getElementById("open-source").innerHTML = phtml;
        document.getElementById("members").innerHTML = mhtml;
        $("#mback").click(function() {
                pmin1 = min1-20;
                if(pmin1 >= 0) {
                min1 -= 20;
                var profileid = 0;
                max1 -= 20;
                mhtml = "";
                $.each(members, function(i, item) {
                    if(profileid < max1 && profileid >= min1) {
                        if (profileid % mpids === 0) {mhtml += "</div><div class='row'>";}
                            mhtml += "<div class='mlistp col text-center'><p>"+i+"</p></div>";
                            
                        }
                    profileid++;
                
        });
    };
        document.getElementById("members").innerHTML = mhtml;
    });
        $("#mnext").click(function() {
            pmax1 = max1+20;
            if(pmax1 <= Object.keys(members).length+20) {
                max1 += 20;
                mhtml = "";
                min1 += 20;
                var profileid = 0;
                $.each(members, function(i, item) {
                    if(profileid < max1 && profileid >= min1) {
                        if (profileid % mpids === 0) {mhtml += "</div><div class='row'>";}
                            mhtml += "<div class='mlistp col text-center'><p>"+i+"</p></div>";
                            
                        }
                    profileid++;
                    
            });
            document.getElementById("members").innerHTML = mhtml;
        };    
    });
        
});
