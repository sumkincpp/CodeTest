
// jquery
$.each(navigator.plugins, function() {
    $('body').append(this.name);
    $('body').append('<br/>');    
});

// console.log!
for (plugin of navigator.plugins) console.log(plugin.name);

