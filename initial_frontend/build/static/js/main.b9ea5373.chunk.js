(window.webpackJsonpinitial_frontend=window.webpackJsonpinitial_frontend||[]).push([[0],{22:function(e,t,a){e.exports=a(48)},27:function(e,t,a){},28:function(e,t,a){e.exports=a.p+"static/media/logo.5d5d9eef.svg"},29:function(e,t,a){},48:function(e,t,a){"use strict";a.r(t);var n=a(0),r=a.n(n),s=a(15),o=a.n(s),c=(a(27),a(16)),u=a(17),i=a(20),l=a(18),d=a(21),m=(a(28),a(29),a(4)),h=a.n(m),f=(a(47),a(50)),p=function(e){function t(e){var a;return Object(c.a)(this,t),(a=Object(i.a)(this,Object(l.a)(t).call(this,e))).next_course_page=function(){console.log("Current Page : "+a.state.page),5!=a.state.page&&h.a.get("course_info/",{auth:{username:"admin11196",password:"adminhassanqrsms"},params:{page:a.state.page+1}}).then((function(e){a.setState((function(t){return{courses_fetched:e.data.results,fetch_staus:!0,page:t.page+1}}))}))},a.course_box=function(e){return r.a.createElement("li",{key:"list_key"+e.course_code},r.a.createElement("div",{className:"card"},r.a.createElement("div",{className:"card-body"},r.a.createElement("h5",{className:"card-title"},e.course_name),r.a.createElement("h6",null,e.course_short),r.a.createElement("p",null,e.course_code))))},a.state={courses_fetched:[],fetch_staus:!0,page:0},a}return Object(d.a)(t,e),Object(u.a)(t,[{key:"componentDidMount",value:function(){var e=this;h.a.get("course_info/",{auth:{username:"admin11196",password:"adminhassanqrsms"},params:{page:1}}).then((function(t){e.setState((function(e){return{courses_fetched:t.data.results,fetch_staus:!0,page:1}})),console.log(t.data)}))}},{key:"render",value:function(){var e=this;return r.a.createElement("div",{className:"container"},r.a.createElement("h1",null," Courses "),r.a.createElement("div",null,r.a.createElement(f.a,{variant:"secondary",onClick:function(){return e.next_course_page()}},"Next Course Page"),r.a.createElement("div",null,this.state.courses_fetched?this.state.courses_fetched.map((function(t){return e.course_box(t)})):r.a.createElement("h2",null," Cant Fetch Courses "))))}}]),t}(r.a.Component);var g=function(){return r.a.createElement("div",{className:"App"},r.a.createElement(p,null))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));o.a.render(r.a.createElement(g,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()}))}},[[22,1,2]]]);
//# sourceMappingURL=main.b9ea5373.chunk.js.map