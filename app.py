from flask import Flask, request, jsonify

app = Flask(__name__)


# # Endpoint to retrieve all tasks
# @app.route("/", methods=["GET"])
# def get_tasks():
#     return jsonify({"tasks": tasks})
# Endpoint to retrieve a specific task by ID
@app.route("/<int:no>", methods=["GET"])
def get_task(no):
  plan_comptable = [{
    "compte": "Encaisse",
    "no": 1010, "type": 1
  }, {
    "compte": "Clients",
    "no": 1100, "type": 1
  }, {
    "compte": "Placements à court terme",
    "no": 1050, "type": 1
  }, {
    "compte": "TPS à recevoir",
    "no": 1105, "type": 1
  }, {
    "compte": "TVQ à recevoir",
    "no": 1110, "type": 1
  }, {
    "compte": "Intérêts à recevoir",
    "no": 1115, "type": 1
  }, {
    "compte": "Honoraires à recevoir",
    "no": 1125, "type": 1
  }, {
    "compte": "Loyers à recevoir",
    "no": 1130, "type": 1
  }, {
    "compte": "Produits divers à recevoir",
    "no": 1145, "type": 1
  }, {
    "compte": "Dividendes à recevoir",
    "no": 1150, "type": 1
  }, {
    "compte": "Taxes à la consommation à recevoir",
    "no": 1155, "type": 1
  }, {
    "compte": "Effet à recevoir (court terme)",
    "no": 1160, "type": 1
  }, {
    "compte": "Stock de marchandises",
    "no": 1180, "type": 1
  }, {
    "compte": "Fournitures de bureau",
    "no": 1190, "type": 1
  }, {
    "compte": "Fournitures (autres)",
    "no": 1200, "type": 1
  }, {
    "compte": "Assurance payée d'avance",
    "no": 1210, "type": 1
  }, {
    "compte": "Loyer payé d'avance",
    "no": 1220, "type": 1
  }, {
    "compte": "Taxes municipales payées d'avance",
    "no": 1230, "type": 1
  }, {
    "compte": "Taxes scolaires payées d'avance",
    "no": 1240, "type": 1
  }, {
    "compte": "Publicité payée d'avance",
    "no": 1250, "type": 1
  }, {
    "compte": "Matériel roulant",
    "no": 1300, "type": 1
  }, {
    "compte": "Amortissement cumulé - matériel roulant",
    "no": 1310, "type": 0
  }, {
    "compte": "Équipement de bureau",
    "no": 1400, "type": 1
  }, {
    "compte": "Amortissement cumulé - équipement de bureau",
    "no": 1410, "type": 0
  }, {
    "compte": "Matériel informatique",
    "no": 1500, "type": 1
  }, {
    "compte": "Amortissement cumulé - matériel informatique",
    "no": 1510, "type": 0
  }, {
    "compte": "Équipement",
    "no": 1600, "type": 1
  }, {
    "compte": "Amortissement cumulé - équipement",
    "no": 1610, "type": 0
  }, {
    "compte": "Ameublement de bureau",
    "no": 1800, "type": 1
  }, {
    "compte": "Amortissement cumulé - ameublement de bureau",
    "no": 1810, "type": 0
  }, {
    "compte": "Améliorations locatives",
    "no": 1850, "type": 1
  }, {
    "compte": "Amortissement cumulé - améliorations locatives",
    "no": 1860, "type": 0
  }, {
    "compte": "Bâtiment",
    "no": 1900, "type": 1
  }, {
    "compte": "Amortissement cumulé - bâtiment",
    "no": 1910, "type": 0
  }, {
    "compte": "Entrepôt",
    "no": 1920, "type": 1
  }, {
    "compte": "Amortissement cumulé - entrepôt",
    "no": 1930, "type": 0
  }, {
    "compte": "Terrain",
    "no": 1960, "type": 1
  }, {
    "compte": "Automobile",
    "no": 1980, "type": 1
  }, {
    "compte": "Emprunt bancaire (marge de crédit)",
    "no": 2050, "type": 0
  }, {
    "compte": "Fournisseurs",
    "no": 2100, "type": 0
  }, {
    "compte": "Effet à payer (court terme)",
    "no": 2150, "type": 0
  }, {
    "compte": "TPS à payer",
    "no": 2305, "type": 0
  }, {
    "compte": "TVQ à payer",
    "no": 2310, "type": 0
  }, {
    "compte": "Salaires à payer",
    "no": 2350, "type": 0
  }, {
    "compte": "RRQ à payer",
    "no": 2360, "type": 0
  }, {
    "compte": "ROAP à payer",
    "no": 2365, "type": 0
  }, {
    "compte": "FSS à payer",
    "no": 2370, "type": 0
  }, {
    "compte": "CNESST à payer",
    "no": 2372, "type": 0
  }, {
    "compte": "Impôt provincial à payer",
    "no": 2375, "type": 0
  }, {
    "compte": "A-E à payer",
    "no": 2390, "type": 0
  }, {
    "compte": "Impôt fédéral à payer",
    "no": 2395, "type": 0
  }, {
    "compte": "Vacances à payer",
    "no": 2400, "type": 0
  }, {
    "compte": "REER collectif à payer",
    "no": 2422, "type": 0
  }, {
    "compte": "RVER à payer",
    "no": 2423, "type": 0
  }, {
    "compte": "Régime de retraite à payer",
    "no": 2425, "type": 0
  }, {
    "compte": "Cotisations syndicales à payer",
    "no": 2430, "type": 0
  }, {
    "compte": "Dons de charité à payer",
    "no": 2435, "type": 0
  }, {
    "compte": "Publicité à payer",
    "no": 2440, "type": 0
  }, {
    "compte": "Intérêts à payer",
    "no": 2450, "type": 0
  }, {
    "compte": "Autres charges à payer",
    "no": 2452, "type": 0
  }, {
    "compte": "Loyer à payer",
    "no": 2455, "type": 0
  }, {
    "compte": "Dividendes à payer",
    "no": 2457, "type": 0
  }, {
    "compte": "Produits perçus d'avance",
    "no": 2460, "type": 0
  }, {
    "compte": "Impôts sur les sociétés à payer",
    "no": 2490, "type": 0
  }, {
    "compte": "Effet à payer (long terme)",
    "no": 2850, "type": 0
  }, {
    "compte": "Emprunt hypothécaire",
    "no": 2900, "type": 0
  }, {
    "compte": "Capital",
    "no": 3100, "type": 0
  }, {
    "compte": "Apport",
    "no": 3200, "type": 0
  }, {
    "compte": "Retrait",
    "no": 3300, "type": 1
  }, {
    "compte": "Capital-actions ordinaire",
    "no": 3400, "type": 0
  }, {
    "compte": "Capital-actions privilégié",
    "no": 3405, "type": 0
  }, {
    "compte": "Bénéfices non-répartis",
    "no": 3475, "type": 0
  }, {
    "compte": "Dividendes-actions ordinaires",
    "no": 3485, "type": 0
  }, {
    "compte": "Dividendes-actions privilégiées",
    "no": 3490, "type": 0
  }, {
    "compte": "Commissions gagnées",
    "no": 4100, "type": 0
  }, {
    "compte": "Honoraires professionnels",
    "no": 4110, "type": 0
  }, {
    "compte": "Services rendus",
    "no": 4120, "type": 0
  }, {
    "compte": "Honoraires de gestion",
    "no": 4130, "type": 0
  }, {
    "compte": "Redevances gagnées",
    "no": 4150, "type": 0
  }, {
    "compte": "Revenus de transport",
    "no": 4160, "type": 0
  }, {
    "compte": "Revenus de location",
    "no": 4170, "type": 0
  }, {
    "compte": "Billets d'entrée",
    "no": 4180, "type": 0
  }, {
    "compte": "Travaux d'excavation",
    "no": 4200, "type": 0
  }, {
    "compte": "Revenus d'extermination",
    "no": 4210, "type": 0
  }, {
    "compte": "Produits divers",
    "no": 4220, "type": 0
  }, {
    "compte": "Honoraires de consultation",
    "no": 4230, "type": 0
  }, {
    "compte": "Produits de livraison",
    "no": 4240, "type": 0
  }, {
    "compte": "Produits d'abonnements gagnés",
    "no": 4250, "type": 0
  }, {
    "compte": "Revenus de cours",
    "no": 4270, "type": 0
  }, {
    "compte": "Produits d'intérêts",
    "no": 4290, "type": 0
  }, {
    "compte": "Produits de dividendes",
    "no": 4300, "type": 0
  }, {
    "compte": "Ventes",
    "no": 4500, "type": 0
  }, {
    "compte": "Rendus et rabais sur ventes",
    "no": 4510, "type": 0
  }, {
    "compte": "Escomptes sur ventes",
    "no": 4520, "type": 0
  }, {
    "compte": "Gain sur disposition d'immobilisations",
    "no": 4640, "type": 0
  }, {
    "compte": "Stock de marchandises au début",
    "no": 5010, "type": 1
  }, {
    "compte": "Achats",
    "no": 5100, "type": 1
  }, {
    "compte": "Rendus et rabais sur achats",
    "no": 5110, "type": 1
  }, {
    "compte": "Escomptes sur achats",
    "no": 5120, "type": 1
  }, {
    "compte": "Frais de transport à l'achat",
    "no": 5130, "type": 1
  }, {
    "compte": "Frais de douane",
    "no": 5140, "type": 1
  }, {
    "compte": "Stock de marchandises à la fin",
    "no": 5150, "type": 1
  }, {
    "compte": "Salaires",
    "no": 5300, "type": 1
  }, {
    "compte": "Salaires des vendeurs",
    "no": 5310, "type": 1
  }, {
    "compte": "Salaires de l'administration",
    "no": 5315, "type": 1
  }, {
    "compte": "Charges sociales",
    "no": 5320, "type": 1
  }, {
    "compte": "Avantages sociaux",
    "no": 5330, "type": 1
  }, {
    "compte": "Vacances",
    "no": 5340, "type": 1
  }, {
    "compte": "Loyer",
    "no": 5410, "type": 1
  }, {
    "compte": "Location de gymnase",
    "no": 5415, "type": 1
  }, {
    "compte": "Publicité",
    "no": 5420, "type": 1
  }, {
    "compte": "Frais de bureau",
    "no": 5500, "type": 1
  }, {
    "compte": "Frais de fournitures (autres)",
    "no": 5530, "type": 1
  }, {
    "compte": "Entretien et réparations - matériel roulant",
    "no": 5600, "type": 1
  }, {
    "compte": "Entretien et réparations - équipement de bureau",
    "no": 5620, "type": 1
  }, {
    "compte": "Entretien et réparations - autres",
    "no": 5630, "type": 1
  }, {
    "compte": "Entretien et réparations - bâtiment",
    "no": 5640, "type": 1
  }, {
    "compte": "Cotisations professionnelles",
    "no": 5650, "type": 1
  }, {
    "compte": "Taxes municipales",
    "no": 5660, "type": 1
  }, {
    "compte": "Taxes scolaires",
    "no": 5670, "type": 1
  }, {
    "compte": "Location d'équipement",
    "no": 5680, "type": 1
  }, {
    "compte": "Frais divers de vente",
    "no": 5690, "type": 1
  }, {
    "compte": "Frais de livraison",
    "no": 5700, "type": 1
  }, {
    "compte": "Frais de déplacement",
    "no": 5705, "type": 1
  }, {
    "compte": "Frais de repas et de représentation",
    "no": 5710, "type": 1
  }, {
    "compte": "Essence",
    "no": 5715, "type": 1
  }, {
    "compte": "Honoraires de gestion",
    "no": 5720, "type": 1
  }, {
    "compte": "Honoraires professionnels",
    "no": 5725, "type": 1
  }, {
    "compte": "Électricité",
    "no": 5730, "type": 1
  }, {
    "compte": "Chauffage",
    "no": 5735, "type": 1
  }, {
    "compte": "Assurance",
    "no": 5740, "type": 1
  }, {
    "compte": "Télécommunications",
    "no": 5750, "type": 1
  }, {
    "compte": "Frais légaux",
    "no": 5760, "type": 1
  }, {
    "compte": "Charges d'intérêts",
    "no": 5780, "type": 1
  }, {
    "compte": "Frais bancaires",
    "no": 5790, "type": 1
  }, {
    "compte": "Charges diverses",
    "no": 5815, "type": 1
  }, {
    "compte": "Amortissement — matériel roulant",
    "no": 5820, "type": 1
  }, {
    "compte": "Amortissement - équipement de bureau",
    "no": 5830, "type": 1
  }, {
    "compte": "Amortissement - matériel informatique",
    "no": 5840, "type": 1
  }, {
    "compte": "Amortissement - équipement",
    "no": 5850, "type": 1
  }, {
    "compte": "Amortissement - ameublement de bureau",
    "no": 5870, "type": 1
  }, {
    "compte": "Amortissement - améliorations locatives",
    "no": 5875, "type": 1
  }, {
    "compte": "Amortissement - bâtiment",
    "no": 5880, "type": 1
  }, {
    "compte": "Amortissement - entrepôt",
    "no": 5885, "type": 1
  }, {
    "compte": "Perte sur disposition d'immobilisations",
    "no": 5900, "type": 1
  }, {
    "compte": "Charge d'impôts sur les sociétés",
    "no": 5995, "type": 1
  }, {
    "compte": "Sommaire des résultats",
    "no": 5999, "type": 1
  }]
  for i in plan_comptable:
    if i["no"] == no:
      return jsonify({"plan_comptable": i})
  return jsonify({"error": "NA"}), 404


# # Endpoint to create a new task
# @app.route("/tasks", methods=["POST"])
# def create_task():
#     data = request.get_json()
#     if "title" not in data:
#         return jsonify({"error": "Title is required"}), 400

#     new_task = {"id": len(tasks) + 1, "title": data["title"], "done": False}
#     tasks.append(new_task)
#     return jsonify({"task": new_task}), 201

# # Endpoint to update an existing task
# @app.route("/tasks/<int:task_id>", methods=["PUT"])
# def update_task(task_id):
#     task = next((task for task in tasks if task["id"] == task_id), None)
#     if task is None:
#         return jsonify({"error": "Task not found"}), 404

#     data = request.get_json()
#     if "title" in data:
#         task["title"] = data["title"]
#     if "done" in data:
#         task["done"] = data["done"]

#     return jsonify({"task": task})

# # Endpoint to delete a task by ID
# @app.route("/tasks/<int:task_id>", methods=["DELETE"])
# def delete_task(task_id):
#     task = next((task for task in tasks if task["id"] == task_id), None)
#     if task is None:
#         return jsonify({"error": "Task not found"}), 404

#     tasks.remove(task)
#     return jsonify({"message": "Task deleted"})

# app.run(host='0.0.0.0', port=81)

if __name__ == "__main__":
    app.run(debug=True, port=5001)