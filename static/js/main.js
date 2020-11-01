function copyToClipboard() {
    var range = document.createRange();
    range.selectNode(document.getElementById("var-list"));
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
    document.execCommand("copy");
    window.getSelection().removeAllRanges();

    $('#clipboard-msg').text("Variant ID's added to clipboard")
    setTimeout(function() {
        $('#clipboard-msg').text("")
    }, 2000)
  }