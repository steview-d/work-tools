function copyToClipboard() {
    var range = document.createRange();
    range.selectNode(document.getElementById("var-list"));
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
    document.execCommand("copy");
    window.getSelection().removeAllRanges();

    $('#btnCopy').html("Copied!")
    setTimeout(function() {
        $('#btnCopy').text("Copy to Clipboard")
    }, 1500)


  }


  