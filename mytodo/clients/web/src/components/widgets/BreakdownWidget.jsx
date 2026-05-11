// mytodo/clients/web/src/components/widgets/BreakdownWidget.jsx

import Widget from './Widget'
import BreakdownBar from './BreakdownBar'


function BreakdownWidget({
  title,
  subtitle,
  items,
  emptyText = '',
  className = '',
}) {
  return (
    <Widget title={title} subtitle={subtitle} className={className}>
      {items.length === 0 ? (
        <p className='widget__muted-text'>{emptyText}</p>
      ) : (
        items.map((item) => (
          <div key={item.label} className='breakdown-widget__item'>
            <div className='breakdown-widget__header'>
              <span className='breakdown-widget__label'>
                {item.label}
                {item.value != null && (
                  <span className='breakdown-widget__count'> ({item.value})</span>
                )}
              </span>
              {item.percentLabel && (
                <span className='breakdown-widget__percent'>{item.percentLabel}</span>
              )}
            </div>
            <BreakdownBar
              percent={item.percent}
              tone={item.tone}
            />
          </div>
        ))
      )}
    </Widget>
  )
}

export default BreakdownWidget
