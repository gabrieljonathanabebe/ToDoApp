// mytodo/clients/web/src/components/widgets/Widget.jsx

import Surface from "../common/Surface";

function Widget({
  title,
  subtitle = '',
  actions = null,
  children,
  className = '',
}) {
  const widgetClassName = ['widget', className]
    .filter(Boolean)
    .join(' ')

  return (
    <Surface
      as="section"
      variant="widget"
      className={widgetClassName}
    >
      {(title || subtitle || actions) && (
        <div className="widget__header">
          <div className="widget__header-text">
            {title && <h3 className="widget__title">{title}</h3>}
            {subtitle && <p className="widget__subtitle">{subtitle}</p>}
          </div>
          {actions && (
            <div className="widget__actions">
              {actions}
            </div>
          )}
        </div>
      )}
      <div className="widget__content">
        {children}
      </div>
    </Surface>
  )
}

export default Widget
