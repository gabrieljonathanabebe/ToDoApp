// mytodo/clients/web/src/components/ui/Badge.jsx


function Badge({ children, tone = 'default', className = '' }) {
  const badgeClassName = [
    'badge',
    tone !== 'default' ? `badge--${tone}` : '',
    className,
  ]
    .filter(Boolean)
    .join(' ')

  return (
    <span className={badgeClassName}>
      {children}
    </span>
  )
}

export default Badge
