import pandas
import matplotlib.pyplot

def prototype_arcan_pruijt():
  file = "prototype-arcan-pruijt.csv"
  df = pandas.read_csv(file)
  data = {}
  for _, row in df.iterrows():
    depId = row['Dependency']
    if depId not in data:
      data[depId] = {'Arcan': 0, 'Prototype': 0, 'Real': 0}
    if row['Arcan'] == 1:
      data[depId]['Arcan'] += 1
    if row['Prototype'] == 1:
      data[depId]['Prototype'] += 1
    data[depId]['Real'] += 1

  Xs_labels = sorted(data.keys())
  Ys_Arcan = [data[label]['Arcan'] for label in Xs_labels]
  Ys_Prototype = [data[label]['Prototype'] for label in Xs_labels]
  Ys_Real = [data[label]['Real'] for label in Xs_labels]

  ndf = pandas.DataFrame({
    'Dependency': Xs_labels,
    'Arcan': Ys_Arcan,
    'Prototype': Ys_Prototype,
    'Real': Ys_Real
  })
  ndf.to_csv('cumulated-prototype-arcan-pruijt.csv', index=False)

  matplotlib.pyplot.figure(figsize=(20,10))
  matplotlib.pyplot.plot(Xs_labels, Ys_Arcan, label='Arcan', marker='o')
  matplotlib.pyplot.plot(Xs_labels, Ys_Prototype, label='Prototype', marker='o')
  matplotlib.pyplot.plot(Xs_labels, Ys_Real, label='Real', marker='o')
  matplotlib.pyplot.legend()
  matplotlib.pyplot.tight_layout()
  matplotlib.pyplot.savefig('prototype-arcan-pruijt.png')

if __name__ == "__main__":
  #prototype_arcan_pruijt()
  pass
