/*!CK:2114680089!*//*1447323623,*/

if (self.CavalryLogger) { CavalryLogger.start_js(["d7V4X"]); }

__d('DetectBrokenProxyCache',['AsyncSignal','Cookie','URI'],function a(b,c,d,e,f,g,h,i,j){if(c.__markCompiled)c.__markCompiled();function k(l,m){var n=i.get(m);if(n!=l&&n!=null&&l!='0'){var o={c:'si_detect_broken_proxy_cache',m:m+' '+l+' '+n},p=new j('/common/scribe_endpoint.php').getQualifiedURI().toString();new h(p,o).send();}}f.exports={run:k};},null);
__d('DimensionLogging',['BanzaiNectar','DOMDimensions'],function a(b,c,d,e,f,g,h,i){if(c.__markCompiled)c.__markCompiled();var j=i.getViewportDimensions();h.log('browser_dimension','homeload',{x:j.width,y:j.height,sw:window.screen.width,sh:window.screen.height,aw:window.screen.availWidth,ah:window.screen.availHeight,at:window.screen.availTop,al:window.screen.availLeft});},null);
__d('DimensionTracking',['Cookie','DOMDimensions','Event','debounce','isInIframe'],function a(b,c,d,e,f,g,h,i,j,k,l){if(c.__markCompiled)c.__markCompiled();function m(){var n=i.getViewportDimensions();h.set('wd',n.width+'x'+n.height);}if(!l()){setTimeout(m,100);j.listen(window,'resize',k(m,250));j.listen(window,'focus',m);}},null);
__d('HighContrastMode',['AccessibilityLogger','CSS','CurrentUser','DOM','Style','URI','emptyFunction'],function a(b,c,d,e,f,g,h,i,j,k,l,m,n){if(c.__markCompiled)c.__markCompiled();var o={init:function(p){var q=new m(window.location.href);if(q.getPath().indexOf('/intern/')===0)return;if(window.top!==window.self)return;var r=k.create('div');k.appendContent(document.body,r);r.style.cssText='border: 1px solid !important;'+'border-color: red green !important;'+'position: fixed;'+'height: 5px;'+'top: -999px;'+'background-image: url('+p.spacerImage+') !important;';var s=l.get(r,'background-image'),t=l.get(r,'border-top-color'),u=l.get(r,'border-right-color'),v=t==u&&(s&&(s=='none'||s=='url(invalid-url:)'));if(v){i.conditionClass(document.documentElement,'highContrast',v);if(j.getID())h.logHCM();}k.remove(r);o.init=n;}};f.exports=o;},null);
__d('Live',['Arbiter','AsyncDOM','AsyncSignal','ChannelConstants','DataStore','DOM','ServerJS','createArrayFromMixed','emptyFunction'],function a(b,c,d,e,f,g,h,i,j,k,l,m,n,o,p){if(c.__markCompiled)c.__markCompiled();function q(s,t){t=JSON.parse(JSON.stringify(t));new n().setRelativeTo(s).handle(t);}var r={logAll:false,startup:function(s){r.logAll=s;r.startup=p;h.subscribe(k.getArbiterType('live'),r.handleMessage.bind(r));},lookupLiveNode:function(s,t){var u=m.scry(document.body,'.live_'+s+'_'+t);u.forEach(function(v){if(l.get(v,'seqnum')===undefined){var w=JSON.parse(v.getAttribute('data-live'));l.set(v,'seqnum',w.seq);}});return u;},handleMessage:function(s,t){var u=t.obj,v=u.fbid,w=u.assoc,x=this.lookupLiveNode(v,w);if(!x)return false;x.forEach(function(y){i.invoke(u.updates,y);if(u.js)q(y,u.js);});},log:function(){if(r.logAll){var s=o(arguments).join(':');new j('/common/scribe_endpoint.php',{c:'live_sequence',m:s}).send();}}};f.exports=r;},null);
__d("UFITracking",["Bootloader"],function a(b,c,d,e,f,g,h){if(c.__markCompiled)c.__markCompiled();function i(k){h.loadModules(["DOM","collectDataAttributes"],function(l,m){k.forEach(function(n){var o=l.scry(document.body,n);if(!o||o.link_data)return;var p=m(o,['ft']).ft;if(Object.keys(p).length){var q=l.create('input',{type:'hidden',name:'link_data',value:JSON.stringify(p)});o.appendChild(q);}});});}var j={addAllLinkData:function(){i(['form.commentable_item']);},addAllLinkDataForQuestion:function(){i(['form.fbEigenpollForm','form.fbQuestionPollForm']);}};f.exports=j;},null);