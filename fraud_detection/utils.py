import pickle


fraudModelsBaseDir = "models/"
fraudModelsSrc = {
    "gradient-boost": "{}".format(fraudModelsBaseDir + "gradient-boost.pkl"),
    "random-forest": "{}".format(fraudModelsBaseDir + "random-forest.pkl"),
    "qfs": "{}".format(fraudModelsBaseDir + "qfs.pkl"),
    "xgb": "{}".format(fraudModelsBaseDir + "xgb.pkl"),
}

fraudModelFeatures = {
    "gradient-boost": [
        "name_email_similarity",
        "velocity_6h",
        "current_address_months_count",
        "housing_status",
    ],
    "random-forest": [
        "name_email_similarity",
        "current_address_months_count",
        "credit_risk_score",
        "housing_status",
    ],
    "qfs": ["name_email_similarity", "bank_branch_count_8w", "housing_status"],
    "xgb": [
        "velocity_6h",
        "employment_status",
        "prev_address_months_count",
        "housing_status",
    ],
}


def getModelFeaturesValues(postDataFeatures):
    features = []
    values = []
    for feature, value in postDataFeatures.items():
        features.append(feature)
        values.append(int(value))
    return features, values


def getFraudModel(model):
    try:
        if fraudModelsSrc[model] == None:
            raise "Fraud detection model requested not found."
        with open(fraudModelsSrc[model], "rb") as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        print("Error loading model:", e)
        raise e


def getCsvLineByIndex(csvReader, index):
    i = 0
    for row in csvReader:
        if i == index:
            return row
        i += 1
    return None


def getModelFeatures(model):
    return fraudModelFeatures[model]
