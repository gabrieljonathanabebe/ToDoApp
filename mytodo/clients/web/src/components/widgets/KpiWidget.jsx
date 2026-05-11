// mytodo/clients/web/src/components/widgets/KpiWidget.jsx

import Widget from "./Widget";
import KpiCard from "./KpiCard";


function KpiWidget({ title, subtitle, items, className = '' }) {
  return (
    <Widget title={title} subtitle={subtitle} className={className}>
      <div className='kpi-widget__grid'>
        {items.map((item) => (
          <KpiCard
            key={item.label}
            label={item.label}
            value={item.value}
            helper={item.helper}
            tone={item.tone}
          />
        ))}
      </div>
    </Widget>
  )
}

export default KpiWidget
