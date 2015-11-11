menu = [
  ['bold', '𝐁', 'Bold']
  ['italic', '𝐼', 'Italic']
  ['blockquote', '’’', 'Quote']
  ['insertUnorderedList', '•', 'Unordered list']
  ['insertOrderedList', '①', 'Ordered list']
  ['p', 'p', 'Paragraph']
  ['superscript', '¹', 'Superscript']
  ['subscript', '₁', 'Subscript']
  ['h1', 'h1', 'Title 1']
  ['h2', 'h2', 'Title 2']
  ['h3', 'h3', 'Title 3']
  ['undo', '↶', 'Undo']
  ['redo', '↷', 'Redo']
  ['source', '<>', 'Source']
]

addEventListener 'DOMContentLoaded', ->
  for textarea in document.querySelectorAll 'textarea[accept=html]'
    do (textarea) ->
      ul = document.createElement 'ul'
      ul.style.fontSize = '0.8em'
      ul.style.margin = '0.25em 0'
      ul.style.opacity = '0.8'
      ul.style.padding = '0'
      for [role, icon, name] in menu
        do (role) ->
          li = document.createElement 'li'
          li.style.display = 'inline-block'

          a = document.createElement 'a'
          a.setAttribute 'href', 'javascript:void(0)'
          a.title = name
          a.text = icon
          a.style.textDecoration = 'none'
          a.style.color = 'inherit'
          a.style.padding = '0.5em'

          if role == 'source'
            a.addEventListener 'click', ->
                [textarea.style.display, div.style.display] = [
                    div.style.display, textarea.style.display]
          else if role in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'blockquote']
            a.addEventListener 'click', ->
              document.execCommand 'formatBlock', false, role
          else
            a.addEventListener 'click', ->
              document.execCommand role, false, null

          li.appendChild a
          ul.appendChild li

      div = document.createElement 'div'
      div.innerHTML = textarea.value
      div.setAttribute 'contenteditable', 'true'

      textarea.parentNode.insertBefore ul, textarea
      textarea.parentNode.insertBefore div, textarea
      textarea.style.display = 'none'

      textarea.addEventListener 'input', ->
        div.innerHTML = textarea.value
      div.addEventListener 'input', ->
        textarea.value = div.innerHTML
