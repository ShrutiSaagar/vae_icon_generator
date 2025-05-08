# Latent Space Exploration of Icons with a Variational Autoencoder

 VAE trained on Heroicon dataset to do arithmetic operations on their vector representations

## Reconstruction sampling
Epoch 6
![reconstruction_epoch_6.png](vae_results/reconstruction_epoch_6.png)

Epoch 12
![reconstruction_epoch_12.png](vae_results/reconstruction_epoch_12.png)

Epoch 36
![reconstruction_epoch_36.png](vae_results/reconstruction_epoch_36.png)

Epoch 48
![reconstruction_epoch_48.png](vae_results/reconstruction_epoch_48.png)

Epoch 50
![reconstruction_epoch_50.png](vae_results/reconstruction_epoch_50.png)


## Random Generated vectors
Epoch 6
![generated_sample_epoch_6.png](vae_results/generated_sample_epoch_6.png)

Epoch 12
![generated_sample_epoch_12.png](vae_results/generated_sample_epoch_12.png)

Epoch 36
![generated_sample_epoch_36.png](vae_results/generated_sample_epoch_36.png)

Epoch 50
![generated_sample_epoch_50.png](vae_results/generated_sample_epoch_50.png)


## Latent Space Interpolation
Interpolating between two random points in the latent space shows smooth transitions between icon styles:
![interpolation_example](vae_results/interpolation/interpolation_7_208_to_169.png)
![interpolation_example](vae_results/interpolation/interpolation_3_498_to_375.png)
![interpolation_example](vae_results/interpolation/interpolation_5_389_to_556.png)
![interpolation_example](vae_results/interpolation/interpolation_6_192_to_593.png)
![interpolation_example](vae_results/interpolation/interpolation_8_106_to_196.png)
![interpolate_example](vae_results/ui_operations/interpolate_55_to_423_20steps.png)
![interpolate_complex_example](vae_results/ui_operations/interpolate_175_to_630_10steps.png)

## Final Results
Final reconstructions and generated samples:
![final_reconstructions.png](vae_results/final_reconstructions.png)
![final_generated_samples.png](vae_results/final_generated_samples.png)

## Icon Arithmetic
Examples of vector arithmetic in the latent space:

### Icon Addition
![sum_example](vae_results/ui_operations/sum_55_423.png)
![sum_complex_example](vae_results/ui_operations/sum_274_266.png)
![sum_complex_example](vae_results/ui_operations/sum_175_630.png)

### Icon Subtraction
![subtract_example](vae_results/ui_operations/subtract_55_423.png)
![subtract_complex_example](vae_results/ui_operations/subtract_175_630.png)
![subtract_complex_example](vae_results/ui_operations/subtract_465_486.png)

### Icon Mean
![mean_example](vae_results/ui_operations/mean_55_423.png)
![mean_complex_example](vae_results/ui_operations/mean_175_630.png)
![mean_complex_example](vae_results/ui_operations/mean_448_267.png)

### Icon Multiplication
![multiply_example](vae_results/ui_operations/multiply_55_423.png)
![multiply_complex_example](vae_results/ui_operations/multiply_274_266.png)
![multiply_complex_example](vae_results/ui_operations/multiply_315_212.png)

### Icon Division
![divide_example](vae_results/ui_operations/divide_55_423.png)
![divide_complex_example](vae_results/ui_operations/divide_448_267.png)
![divide_complex_example](vae_results/ui_operations/divide_512_205.png)


## Model Architecture
The VAE consists of an encoder and decoder with the following structure:
- Encoder: Convolutional layers (32→64→128→256)
- Latent dimension: 32
- Decoder: Transposed convolutions (256→128→64→32)

## Training Details
- Epochs: 50
- Batch size: 32
- Learning rate: 0.0001
- Beta (KL weight): 1.0
- Optimizer: Adam

![Train kl loss](vae_results/train_kl_loss.png)
![Train recon loss](vae_results/train_recon_loss.png)
