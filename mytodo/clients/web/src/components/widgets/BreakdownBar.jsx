// mytodo/clients/web/src/components/widgets/BreakdownBar.jsx

function BreakdownBar({ percent = 0, tone = 'default' }) {
  const safePercent = Math.max(0, Math.min(percent, 100))

  const fillClassName = [
    'breakdown-bar__fill',
    tone !== 'default' ? `breakdown-bar__fill--${tone}` : '',
  ]
    .filter(Boolean)
    .join(' ')

  return (
    <div className='breakdown-bar'>
      <div
        className={fillClassName}
        style={{ width: `${safePercent}%` }}
      />
    </div>
  )
}

export default BreakdownBar
