ADVISORY = {
    'Potato___Early_blight': {
        'description': 'Early blight is a fungal disease that affects potato leaves.',
        'causes': 'Caused by the fungus Alternaria solani.',
        'symptoms': 'Dark spots with concentric rings on older leaves.',
        'treatment': 'Remove infected leaves and apply fungicide.',
        'prevention': 'Crop rotation and resistant varieties.'
    },
    'Potato___Late_blight': {
        'description': 'Late blight causes brown lesions on foliage.',
        'causes': 'Phytophthora infestans infection.',
        'symptoms': 'Dark, water-soaked spots that spread quickly.',
        'treatment': 'Use copper-based fungicides and remove debris.',
        'prevention': 'Avoid overhead watering and use resistant cultivars.'
    },
    'Potato___healthy': {
        'description': 'No disease detected.',
        'causes': 'Healthy plant.',
        'symptoms': 'Normal green leaves.',
        'treatment': 'N/A',
        'prevention': 'Maintain regular care.'
    },
    'Corn___Cercospora_leaf_spot_Gray_leaf_spot': {
        'description': 'Fungal spot disease of corn leaves.',
        'causes': 'Infection by Cercospora spp.',
        'symptoms': 'Grayish spots with dark borders.',
        'treatment': 'Apply appropriate fungicides.',
        'prevention': 'Rotate crops and remove residue.'
    },
    'Corn___Common_rust': {
        'description': 'Rust disease producing orange pustules.',
        'causes': 'Puccinia sorghi pathogen.',
        'symptoms': 'Orange-red pustules on leaves.',
        'treatment': 'Use fungicide sprays.',
        'prevention': 'Plant resistant hybrids.'
    },
    'Corn___Northern_Leaf_Blight': {
        'description': 'Fungal disease causing large lesions.',
        'causes': 'Helminthosporium maydis fungus.',
        'symptoms': 'Elongated gray-green lesions.',
        'treatment': 'Fungicide application.',
        'prevention': 'Use resistant varieties and crop rotation.'
    },
    'Corn___healthy': {
        'description': 'No disease detected.',
        'causes': 'Healthy plant.',
        'symptoms': 'Normal appearance.',
        'treatment': 'N/A',
        'prevention': 'Maintain good agronomy.'
    },
    'Grape___Black_rot': {
        'description': 'Fungal rot affecting grapes.',
        'causes': 'Guignardia bidwellii.',
        'symptoms': 'Black lesions on leaves and fruit.',
        'treatment': 'Cut and destroy infected material.',
        'prevention': 'Apply fungicides regularly.'
    },
    'Grape___Esca_(Black_Measles)': {
        'description': 'Disease causing black spots on grapes.',
        'causes': 'Multiple fungal pathogens.',
        'symptoms': 'Black lesions and gummy exudates.',
        'treatment': 'Remove infected wood.',
        'prevention': 'Maintain vine health and sanitation.'
    },
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': {
        'description': 'Leaf spot disease on grapes.',
        'causes': 'Isariopsis ilicifolia.',
        'symptoms': 'Small chlorotic spots that enlarge.',
        'treatment': 'Fungicide sprays.',
        'prevention': 'Improve air circulation.'
    },
    'Grape___healthy': {
        'description': 'No disease detected.',
        'causes': 'Healthy plant.',
        'symptoms': 'Normal leaves.',
        'treatment': 'N/A',
        'prevention': 'Standard care.'
    },
}


def get_advice(class_name):
    return ADVISORY.get(class_name, {})
