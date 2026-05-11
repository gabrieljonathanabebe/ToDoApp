// mytodo/clients/web/src/components/common/Panel.jsx

import Surface from './Surface'

function Panel({ children, className = '' }) {
  return (
    <Surface variant='panel' className={className}>
      {children}
    </Surface>
  )
}

export default Panel
