(function(t){function e(e){for(var r,i,l=e[0],s=e[1],c=e[2],p=0,f=[];p<l.length;p++)i=l[p],Object.prototype.hasOwnProperty.call(o,i)&&o[i]&&f.push(o[i][0]),o[i]=0;for(r in s)Object.prototype.hasOwnProperty.call(s,r)&&(t[r]=s[r]);u&&u(e);while(f.length)f.shift()();return a.push.apply(a,c||[]),n()}function n(){for(var t,e=0;e<a.length;e++){for(var n=a[e],r=!0,l=1;l<n.length;l++){var s=n[l];0!==o[s]&&(r=!1)}r&&(a.splice(e--,1),t=i(i.s=n[0]))}return t}var r={},o={app:0},a=[];function i(e){if(r[e])return r[e].exports;var n=r[e]={i:e,l:!1,exports:{}};return t[e].call(n.exports,n,n.exports,i),n.l=!0,n.exports}i.m=t,i.c=r,i.d=function(t,e,n){i.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:n})},i.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},i.t=function(t,e){if(1&e&&(t=i(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var n=Object.create(null);if(i.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var r in t)i.d(n,r,function(e){return t[e]}.bind(null,r));return n},i.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return i.d(e,"a",e),e},i.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},i.p="/";var l=window["webpackJsonp"]=window["webpackJsonp"]||[],s=l.push.bind(l);l.push=e,l=l.slice();for(var c=0;c<l.length;c++)e(l[c]);var u=s;a.push([0,"chunk-vendors"]),n()})({0:function(t,e,n){t.exports=n("56d7")},"034f":function(t,e,n){"use strict";n("85ec")},"0681":function(t,e,n){t.exports=n.p+"img/sheep_1.535dca05.png"},"56d7":function(t,e,n){"use strict";n.r(e);n("e260"),n("e6cf"),n("cca6"),n("a79d");var r=n("2b0e"),o=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"app"}},[n("Home")],1)},a=[],i=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("div",{staticClass:"row ml-3 mr-3"},[r("div",{staticClass:"col"},[r("input",{directives:[{name:"model",rawName:"v-model",value:t.url,expression:"url"}],staticClass:"input_1",attrs:{type:"text",placeholder:"URL to shorten"},domProps:{value:t.url},on:{input:function(e){e.target.composing||(t.url=e.target.value)}}}),r("a",{staticClass:"btn btn-lg btn-success mt-5",attrs:{href:"javascript:void(0)"},on:{click:t.getShortLink}},[t._v("Get short link")]),t.link.follow_url?r("div",{staticClass:"bg-light p-2 mt-5"},[r("h1",{attrs:{id:"url_h1"},on:{click:t.copyTextToClipboard}},[t._v(t._s(t.link.follow_url))]),t.link?r("h5",{staticClass:"mt-4"},[t._v("Original: "+t._s(t.link.original_url.substring(0,30)))]):t._e()]):r("div",{staticClass:"p-2 mt-5"},[r("h1",{attrs:{id:"url_h1"}},[t._v("... meh ...")])]),t._m(0)]),r("div",{staticClass:"col text-center"},[r("h1",{attrs:{id:"title"}},[t._v("wools.cc")]),r("div",[t.ewe_image_1?r("img",{attrs:{width:"500",src:n("0681"),alt:"wools ewe"}}):r("img",{attrs:{width:"600",src:n("d111"),alt:"wools ewe"}})])])])])},l=[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"row mt-5"},[n("div",{staticClass:"col"},[n("p",[t._v("That's Baaarbara, by the way, and she follows *anything*! If you ask me, I would say she's a sheep...")]),n("p",[t._v("Links are valid for "),n("strong",[t._v("30 days")]),t._v(" and then they are turned into woolly jumpers... meh.")])])])}],s=(n("99af"),n("9911"),n("bc3a")),c=n.n(s),u={name:"Home",data:function(){return{url:"",link:!1,ewe_image_1:!0}},methods:{getShortLink:function(){var t=this;this.ewe_image_1=!this.ewe_image_1,""!=this.url&&c.a.get("".concat(k,"?url=").concat(this.url)).then((function(e){console.log(e),t.url="",t.link=e.data})).catch((function(t){alert(t)}))},copyTextToClipboard:function(){navigator.clipboard.writeText(this.link.follow_url).then((function(){console.log("Async: Copying to clipboard was successful!")}),(function(t){console.error("Async: Could not copy text: ",t)}))}}},p=u,f=(n("8b71"),n("2877")),d=Object(f["a"])(p,i,l,!1,null,null,null),h=d.exports,v={name:"App",components:{Home:h}},m=v,_=(n("034f"),Object(f["a"])(m,o,a,!1,null,null,null)),g=_.exports,b=n("5f5b"),w=n("b1e0");n("f9e3"),n("2dd8");r["default"].use(b["a"]),r["default"].use(w["a"]),r["default"].config.productionTip=!1;var y="https://wools.cc";new r["default"]({render:function(t){return t(g)}}).$mount("#app");var k=e["default"]=y},"85ec":function(t,e,n){},"88d7":function(t,e,n){},"8b71":function(t,e,n){"use strict";n("88d7")},d111:function(t,e,n){t.exports=n.p+"img/sheep_2.28c53de3.png"}});
//# sourceMappingURL=app.de0c0878.js.map