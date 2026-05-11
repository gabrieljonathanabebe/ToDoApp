// mytodo/clients/web/src/components/common/Surface.jsx

function Surface({
  as: Component = 'div',
  variant = 'panel',
  interactive = false,
  className = '',
  children,
  ...props
}) {
  const surfaceClassName = [
    'surface',
    `surface-${variant}`,
    interactive ? 'surface-interactive' : '',
    className,
  ]
    .filter(Boolean)
    .join(' ')

  return (
    <Component className={surfaceClassName} {...props}>
      {children}
    </Component>
  )
}

export default Surface
