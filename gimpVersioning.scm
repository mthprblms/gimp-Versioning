;;; Save Version Script
(define (save-version image drawable)
    (let* (
        (filename (car (gimp-image-get-filename image)))
        (version-number (car (gimp-image-get-vectors image)))
        (extension-start (- (string-length filename) (string-search-reverse "." filename)))
        (filename-base (substring filename 0 extension-start))
        (filename-extension (substring filename extension-start))
        (version-filename (string-append filename-base "_v" (number->string version-number) filename-extension))
        (new-image (car (gimp-image-duplicate image)))
    )
        (gimp-image-undo-enable new-image)
        (gimp-image-set-filename new-image version-filename)
        (gimp-image-flatten new-image)
        (file-xcf-save 1 new-image drawable version-filename version-filename 0 0)
        (gimp-image-delete new-image)
    )
)

;;; Register the script
(script-fu-register "save-version"
    "Save Version"
    "Save the current version of the image"
    "Author Name"
    "Author Name"
    "2024"
    ""
    SF-IMAGE "Image" 0
    SF-DRAWABLE "Drawable" 0
)

;;; Attach the script to a menu item
(script-fu-menu-register "save-version"
    "<Image>/File/Save Version"
)
