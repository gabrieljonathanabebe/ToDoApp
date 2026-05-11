// mytodo/clients/web/src/components/widgets/KpiCard.jsx


function KpiCard({ label, value, helper = '', tone = 'default' }) {
  const valueClassName = [
    'kpi-card__value',
    tone !== 'default' ? `kpi-card__value--${tone}` : '',
  ]
    .filter(Boolean)
    .join(' ')

  return (
    <div className='kpi-card'>
      <span className='kpi-card__label'>{label}</span>
      <strong className={valueClassName}>{value}</strong>
      {helper && <span className='kpi-card__helper'>{helper}</span>}
    </div>
  )
}

export default KpiCard
