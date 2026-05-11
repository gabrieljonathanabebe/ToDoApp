// mytodo/clients/web/src/components/common/PopoverMenu.jsx

import { useRef } from "react";
import useClickOutside from '../../hooks/useClickOutside'
import Surface from "./Surface";


function PopoverMenu({
  show,
  onClose,
  trigger,
  children,
  anchorClassName = '',
  menuClassName = '',
  placement = 'bottom'
}) {
  const menuRef = useRef(null)

  useClickOutside(menuRef, () => {
    if (show) onClose()
  })
  return (
    <div className={`popover-anchor ${anchorClassName}`.trim()} ref={menuRef}>
      {trigger}
      {show && (
        <Surface
          variant='dropdown'
          className={`
            popover-menu
            ${placement === 'top' ? 'popover-menu--top' : ''}
            ${menuClassName}
          `.trim()}
        >
          {children}
        </Surface>
      )}
    </div>
  )
}


export default PopoverMenu
