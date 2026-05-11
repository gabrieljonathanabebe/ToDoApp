// mytodo/clients/web/src/components/common/EmptyState.jsx

import Surface from "./Surface"


function EmptyState({ icon, title, description }) {
  const Icon = icon

  return (
    <Surface variant="panel" className="state-card">
      <div className="state-icon-wrap">
        <Icon className="state-icon state-icon-primary" size={28} strokeWidth={2} />
      </div>
      <h2 className="state-title">{title}</h2>
      <p className="state-description">{description}</p>
    </Surface>
  )
}

export default EmptyState
