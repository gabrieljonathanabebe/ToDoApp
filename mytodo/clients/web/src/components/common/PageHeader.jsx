// mytodo/clients/web/src/components/common/PageHeader.jsx


function PageHeader({
  title,
  icon: Icon = null,
  actions = null,
  variant = 'page',
  as: TitleComponent = 'h1',
  className = '',
}) {
  const headerClassName = [
    'page-header',
    `page-header--${variant}`,
    className,
  ]
    .filter(Boolean)
    .join(' ')

  return (
    <div className={headerClassName}>
      <div className='page-header__title-row'>
        {Icon && (
          <Icon
            className='page-header__icon'
            size={variant === 'section' ? 18 : 24}
            strokeWidth={2.2}
          />
        )}
        <TitleComponent className='page-header__title'>
          {title}
        </TitleComponent>
      </div>
      {actions && (
        <div className='page-header__actions'>
          {actions}
        </div>
      )}
    </div>
  )
}

export default PageHeader
