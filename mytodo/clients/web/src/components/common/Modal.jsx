// mytodo/clients/web/src/components/common/Modal.jsx

import { useEffect } from "react";
import { createPortal } from "react-dom";
import { X } from "lucide-react";

import Surface from "./Surface";


function Modal({
  open,
  title,
  onClose,
  children,
  className = '',
  labelledBy = 'modal-title',
}) {
  useEffect(() => {
    if (!open) return

    function handleKeyDown(event) {
      if (event.key === 'Escape') {
        onClose()
      }
    }

    window.addEventListener('keydown', handleKeyDown)
    return () => window.removeEventListener('keydown', handleKeyDown)
  }, [open, onClose])

  if (!open) return null

  return createPortal(
    <div className="modal-backdrop" onClick={onClose}>
      <Surface
        as="section"
        variant="modal"
        className={`modal ${className}`.trim()}
        role='dialog'
        aria-modal='true'
        aria-labelledby={labelledBy}
        onClick={(event) => event.stopPropagation()}
      >
        <div className="modal-header">
          <h3 id={labelledBy} className="modal-title">
            {title}
          </h3>
          <button
            type="button"
            className="icon-action icon-action-plain"
            onClick={onClose}
            aria-label="Close modal"
            title="Close"
          >
            <X size={18} strokeWidth={2} />
          </button>
        </div>
        <div className="modal-content">
          {children}
        </div>
      </Surface>
    </div>,
    document.body
  )
}

export default Modal
