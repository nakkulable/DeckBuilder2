/*
jQWidgets v3.3.0 (2014-May-26)
Copyright (c) 2011-2014 jQWidgets.
License: http://jqwidgets.com/license/
*/

(function(a){a.jqx.jqxWidget("jqxSwitchButton","",{});a.extend(a.jqx._jqxSwitchButton.prototype,{defineInstance:function(){this.disabled=false;this.checked=false;this.onLabel="On";this.offLabel="Off";this.toggleMode="default";this.animationDuration=250;this.width=90;this.height=30;this.animationEnabled=true;this.thumbSize="40%";this.orientation="horizontal";this.switchRatio="50%";this.metroMode=false;this._isMouseDown=false;this.rtl=false;this._dimensions={horizontal:{size:"width",opSize:"height",oSize:"outerWidth",opOSize:"outerHeight",pos:"left",oPos:"top",opposite:"vertical"},vertical:{size:"height",opSize:"width",oSize:"outerHeight",opOSize:"outerWidth",pos:"top",oPos:"left",opposite:"horizontal"}};this._touchEvents={mousedown:"touchstart",click:"touchend",mouseup:"touchend",mousemove:"touchmove",mouseenter:"mouseenter",mouseleave:"mouseleave"};this._borders={};this._isTouchDevice=false;this._distanceRequired=3;this._isDistanceTraveled=false;this._thumb;this._onLabel;this._offLabel;this._wrapper;this._animationActive=false;this.aria={"aria-checked":{name:"checked",type:"boolean"},"aria-disabled":{name:"disabled",type:"boolean"}};this._events=["checked","unchecked","change"]},createInstance:function(b){if(this.element.nodeName){if(this.element.nodeName=="INPUT"||this.element.nodeName=="BUTTON"){throw"jqxSwitchButton can be rendered only from a DIV tag."}}this.host.attr("role","checkbox");a.jqx.aria(this);this.render();var c=this;a.jqx.utilities.resize(this.host,function(){c.render()})},resize:function(c,b){this.width=c;this.height=b;this.render()},render:function(){this.innerHTML="";if(this.theme&&this.theme!=""&&(this.theme.indexOf("metro")!=-1||this.theme.indexOf("windowsphone")!=-1||this.theme.indexOf("office")!=-1)){if(this.thumbSize=="40%"){this.thumbSize=12}this.metroMode=true}var c=a.data(document.body,"jqx-switchbutton")||1;this._idHandler(c);a.data(document.body,"jqx-draggables",++c);this._isTouchDevice=a.jqx.mobile.isTouchDevice();this.switchRatio=parseInt(this.switchRatio,10);this._render();this._addClasses();this._performLayout();this._removeEventHandlers();this._addEventHandles();this._disableSelection();var b=this;if(!this.checked){this._switchButton(false,0,true)}if(this.disabled){this.element.disabled=true}},setOnLabel:function(b){this._onLabel.html('<div style="display: inline-block;">'+b+"</div>");this._centerLabels()},setOffLabel:function(b){this._offLabel.html('<div style="display: inline-block;">'+b+"</div>");this._centerLabels()},toggle:function(){if(this.checked){this.uncheck()}else{this.check()}},val:function(b){if(arguments.length==0||(b!=null&&typeof(b)=="object")){return this.checked}if(typeof b=="string"){if(b=="true"){this.check()}if(b=="false"){this.uncheck()}if(b==""){this.indeterminate()}}else{if(b==true){this.check()}if(b==false){this.uncheck()}if(b==null){this.indeterminate()}}return this.checked},uncheck:function(){var b=this;this._switchButton(false);a.jqx.aria(this,"aria-checked",this.checked)},check:function(){var b=this;this._switchButton(true);a.jqx.aria(this,"aria-checked",this.checked)},_idHandler:function(b){if(!this.element.id){var c="jqx-switchbutton-"+b;this.element.id=c}},_dir:function(b){return this._dimensions[this.orientation][b]},_getEvent:function(c){if(this._isTouchDevice){var b=this._touchEvents[c];return a.jqx.mobile.getTouchEventName(b)}else{return c}},_render:function(){this._thumb=a("<div/>");this._onLabel=a("<div/>");this._offLabel=a("<div/>");this._wrapper=a("<div/>");this._onLabel.appendTo(this.host);this._thumb.appendTo(this.host);this._offLabel.appendTo(this.host);this.host.wrapInner(this._wrapper);this._wrapper=this.host.children();this.setOnLabel(this.onLabel);this.setOffLabel(this.offLabel)},_addClasses:function(){var c=this._thumb,d=this._onLabel,b=this._offLabel;this.host.addClass(this.toThemeProperty("jqx-switchbutton"));this.host.addClass(this.toThemeProperty("jqx-widget"));this.host.addClass(this.toThemeProperty("jqx-widget-content"));this._wrapper.addClass(this.toThemeProperty("jqx-switchbutton-wrapper"));c.addClass(this.toThemeProperty("jqx-fill-state-normal"));c.addClass(this.toThemeProperty("jqx-switchbutton-thumb"));d.addClass(this.toThemeProperty("jqx-switchbutton-label-on"));d.addClass(this.toThemeProperty("jqx-switchbutton-label"));b.addClass(this.toThemeProperty("jqx-switchbutton-label-off"));b.addClass(this.toThemeProperty("jqx-switchbutton-label"));if(this.checked){this.host.addClass(this.toThemeProperty("jqx-switchbutton-on"))}else{this.host.removeClass(this.toThemeProperty("jqx-switchbutton-on"))}},_performLayout:function(){var g=this.host,e=this._dir("opSize"),f=this._dir("size"),i=this._wrapper,d;g.css({width:this.width,height:this.height});i.css(e,g[e]());this._thumbLayout();this._labelsLayout();d=this._borders[this._dir("opposite")];i.css(f,g[f]()+this._offLabel[this._dir("oSize")]()+d);i.css(e,g[e]());if(this.metroMode||(this.theme&&this.theme!=""&&(this.theme.indexOf("metro")!=-1||this.theme.indexOf("office")!=-1))){var c=this._thumb,h=this._onLabel,b=this._offLabel;h.css("position","relative");h.css("top","1px");h.css("margin-left","1px");b.css("position","relative");b.css("top","1px");b.css("left","-2px");b.css("margin-right","1px");b.height(h.height()-2);b.width(h.width()-3);h.height(h.height()-2);h.width(h.width()-3);this._thumb[this._dir("size")](this.thumbSize+3);this._thumb.css("top","-1px");this._thumb[this._dir("opSize")](g[this._dir("opSize")]()+2);this._thumb.css("position","relative");this.host.css("overflow","hidden");if(this.checked){this._onLabel.css("visibility","visible");this._offLabel.css("visibility","hidden");this._thumb.css("left","0px")}else{this._onLabel.css("visibility","hidden");this._offLabel.css("visibility","visible");this._thumb.css("left","-2px")}}},_thumbLayout:function(){var d=this.thumbSize,e=this.host,b=0,f={horizontal:0,vertical:0},c=this;if(d.toString().indexOf("%")>=0){d=e[this._dir("size")]()*parseInt(d,10)/100}this._thumb[this._dir("size")](d);this._thumb[this._dir("opSize")](e[this._dir("opSize")]());this._handleThumbBorders()},_handleThumbBorders:function(){this._borders.horizontal=parseInt(this._thumb.css("border-left-width"),10)||0;this._borders.horizontal+=parseInt(this._thumb.css("border-right-width"),10)||0;this._borders.vertical=parseInt(this._thumb.css("border-top-width"),10)||0;this._borders.vertical+=parseInt(this._thumb.css("border-bottom-width"),10)||0;var b=this._borders[this._dir("opposite")];if(this.orientation==="horizontal"){this._thumb.css("margin-top",-b/2);this._thumb.css("margin-left",0)}else{this._thumb.css("margin-left",-b/2);this._thumb.css("margin-top",0)}},_labelsLayout:function(){var g=this.host,c=this._thumb,e=this._dir("opSize"),h=this._dir("size"),b=this._dir("oSize"),f=g[h]()-c[b](),d=this._borders[this._dir("opposite")]/2;this._onLabel[h](f+d);this._offLabel[h](f+d);if(this.rtl){this._onLabel[h](f+2*d)}this._onLabel[e](g[e]());this._offLabel[e](g[e]());this._orderLabels();this._centerLabels()},_orderLabels:function(){if(this.orientation==="horizontal"){var b="left";if(this.rtl){b="right"}this._onLabel.css("float",b);this._thumb.css("float",b);this._offLabel.css("float",b)}else{this._onLabel.css("display","block");this._offLabel.css("display","block")}},_centerLabels:function(){var c=this._onLabel.children("div"),b=this._offLabel.children("div"),e=c.parent(),f=e.height(),g=c.outerHeight(),d=this._borders[this.orientation]/2||0;if(g==0){g=14}var h=Math.floor((f-g)/2)+d;c.css("margin-top",h);b.css("margin-top",h)},_removeEventHandlers:function(){var b="."+this.element.id;this.removeHandler(this._wrapper,this._getEvent("click")+b+this.element.id,this._clickHandle);this.removeHandler(this._thumb,this._getEvent("mousedown")+b,this._mouseDown);this.removeHandler(a(document),this._getEvent("mouseup")+b,this._mouseUp);this.removeHandler(a(document),this._getEvent("mousemove")+b,this._mouseMove)},_addEventHandles:function(){var c="."+this.element.id,b=this;this.addHandler(this._thumb,"mouseenter"+c,function(){b._thumb.addClass(b.toThemeProperty("jqx-fill-state-hover"))});this.addHandler(this._thumb,"mouseleave"+c,function(){b._thumb.removeClass(b.toThemeProperty("jqx-fill-state-hover"))});this.addHandler(this._wrapper,this._getEvent("click")+c,this._clickHandle,{self:this});this.addHandler(this._thumb,this._getEvent("mousedown")+c,this._mouseDown,{self:this});this.addHandler(a(document),this._getEvent("mouseup")+c,this._mouseUp,{self:this});this.addHandler(a(document),this._getEvent("mousemove")+c,this._mouseMove,{self:this})},enable:function(){this.disabled=false;this.element.disabled=false;a.jqx.aria(this,"aria-disabled",this.disabled)},disable:function(){this.disabled=true;this.element.disabled=true;a.jqx.aria(this,"aria-disabled",this.disabled)},_clickHandle:function(c){var b=c.data.self;if((b.toggleMode==="click"||b.toggleMode==="default")&&!b.disabled){if(!b._isDistanceTraveled&&!b._dragged){b._wrapper.stop();b.toggle()}}b._thumb.removeClass(b.toThemeProperty("jqx-fill-state-pressed"))},_mouseDown:function(c){var b=c.data.self,d=b._wrapper;if(b.metroMode){b.host.css("overflow","hidden");b._onLabel.css("visibility","visible");b._offLabel.css("visibility","visible")}b._mouseStartPosition=b._getMouseCoordinates(c);b._buttonStartPosition={left:parseInt(d.css("margin-left"),10)||0,top:parseInt(d.css("margin-top"),10)||0};if(!b.disabled&&(b.toggleMode==="slide"||b.toggleMode==="default")){b._wrapper.stop();b._isMouseDown=true;b._isDistanceTraveled=false;b._dragged=false}b._thumb.addClass(b.toThemeProperty("jqx-fill-state-pressed"))},_mouseUp:function(d){var c=d.data.self;if(c.metroMode){}c._isMouseDown=false;c._thumb.removeClass(c.toThemeProperty("jqx-fill-state-pressed"));if(!c._isDistanceTraveled){return}var f=c._wrapper,b=parseInt(f.css("margin-"+c._dir("pos")),10)||0,e=c._dropHandler(b);if(e){c._switchButton(!c.checked)}else{c._switchButton(c.checked,null,true)}c._isDistanceTraveled=false},_mouseMove:function(f){var d=f.data.self,b=d._getMouseCoordinates(f);if(d._isMouseDown&&d._distanceTraveled(b)){var e=d._dir("pos"),h=d._wrapper,c=d._buttonStartPosition[e],g=c+b[e]-d._mouseStartPosition[e],g=d._validatePosition(g);d._dragged=true;h.css("margin-"+d._dir("pos"),g);d._onLabel.css("visibility","visible");d._offLabel.css("visibility","visible");return false}},_distanceTraveled:function(b){if(this._isDistanceTraveled){return true}else{if(!this._isMouseDown){return false}else{var d=this._mouseStartPosition,c=this._distanceRequired;this._isDistanceTraveled=Math.abs(b.left-d.left)>=c||Math.abs(b.top-d.top)>=c;return this._isDistanceTraveled}}},_validatePosition:function(c){var d=this._borders[this._dir("opposite")],b=0,e=-(this.host[this._dir("size")]()-this._thumb[this._dir("oSize")]())-d;if(b<c){return b}if(e>c){return e}return c},_dropHandler:function(c){var b=0,d=-(this.host[this._dir("size")]()-this._thumb[this._dir("oSize")]()),g=Math.abs(d-b),e=Math.abs(c-this._buttonStartPosition[this._dir("pos")]),f=g*(this.switchRatio/100);if(e>=f){return true}return false},_switchButton:function(c,h,g){if(this.metroMode){this.host.css("overflow","hidden");this._onLabel.css("visibility","visible");this._offLabel.css("visibility","visible");if(c){this._thumb.css("left","0px")}else{this._thumb.css("left","-2px")}}else{this._onLabel.css("visibility","visible");this._offLabel.css("visibility","visible")}var i=this._wrapper,d=this,f={},e=this._borders[this._dir("opposite")],b=0;if(typeof h==="undefined"){h=(this.animationEnabled?this.animationDuration:0)}if(!this.rtl){if(!c){b=this.host[this._dir("size")]()-this._thumb[this._dir("oSize")]()+e}}else{if(c){b=this.host[this._dir("size")]()-this._thumb[this._dir("oSize")]()+e;if(this.metroMode){b+=5}}else{if(this.metroMode){b-=3}}}f["margin-"+this._dir("pos")]=-b;if(c){d.host.addClass(d.toThemeProperty("jqx-switchbutton-on"))}else{d.host.removeClass(d.toThemeProperty("jqx-switchbutton-on"))}i.animate(f,h,function(){if(c){d._onLabel.css("visibility","visible");d._offLabel.css("visibility","hidden")}else{d._onLabel.css("visibility","hidden");d._offLabel.css("visibility","visible")}d.checked=c;if(!g){d._handleEvent(!c)}})},_handleEvent:function(b){if(b!==this.checked){this._raiseEvent(2,{check:this.checked,checked:this.checked})}if(b){this._raiseEvent(0,{checked:this.checked})}else{this._raiseEvent(1,{checked:this.checked})}},_disableSelection:function(){var c=this.host,b=c.find("*");a.each(b,function(d,e){e.onselectstart=function(){return false};a(e).addClass("jqx-disableselect")})},_getMouseCoordinates:function(b){if(this._isTouchDevice){return{left:b.originalEvent.touches[0].pageX,top:b.originalEvent.touches[0].pageY}}else{return{left:b.pageX,top:b.pageY}}},destroy:function(){this._removeEventHandlers();this.host.removeClass(this.toThemeProperty("jqx-switchbutton"));this._wrapper.remove()},_raiseEvent:function(d,b){var c=a.Event(this._events[d]);c.args=b;return this.host.trigger(c)},_themeChanger:function(f,g,e){if(!f){return}if(typeof e==="undefined"){e=this.host}var h=e[0].className.split(" "),b=[],j=[],d=e.children();for(var c=0;c<h.length;c+=1){if(h[c].indexOf(f)>=0){b.push(h[c]);j.push(h[c].replace(f,g))}}this._removeOldClasses(b,e);this._addNewClasses(j,e);for(var c=0;c<d.length;c+=1){this._themeChanger(f,g,a(d[c]))}},_removeOldClasses:function(d,c){for(var b=0;b<d.length;b+=1){c.removeClass(d[b])}},_addNewClasses:function(d,c){for(var b=0;b<d.length;b+=1){c.addClass(d[b])}},propertyChangedHandler:function(b,c,e,d){switch(c){case"disabled":if(d){this.disable()}else{this.enable()}break;case"switchRatio":this.switchRatio=parseInt(this.switchRatio,10);break;case"checked":if(d){this.check()}else{this.uncheck()}break;case"onLabel":this.setOnLabel(d);break;case"offLabel":this.setOffLabel(d);break;case"theme":a.jqx.utilities.setTheme(e,d,b.host);break;case"width":case"height":case"thumbSize":case"orientation":this._performLayout();this._wrapper.css("left",0);this._wrapper.css("top",0);this._switchButton(this.checked,0,true);break}}})})(jQuery);